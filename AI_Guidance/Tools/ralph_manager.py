#!/usr/bin/env python3
"""
Ralph Manager - Long-running task management for memail

Manages background tasks like test suites, builds, and linting that
may take longer than typical Claude Code tool timeouts.

Usage:
    python ralph_manager.py --status                    # Show all tasks
    python ralph_manager.py --run "pytest" --name tests # Start task
    python ralph_manager.py --check <task_id>           # Check specific task
    python ralph_manager.py --kill <task_id>            # Kill task
    python ralph_manager.py --clean                     # Clean completed tasks
"""

import os
import sys
import json
import argparse
import subprocess
import signal
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Any

# Add common to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'common'))
import config_loader

# Configuration
ralph_config = config_loader.get_ralph_config()
STATE_FILE = ralph_config.get('state_path', Path('.ralph_state.json'))
DEFAULT_TIMEOUT = ralph_config.get('default_timeout', 300)


def load_state() -> Dict[str, Any]:
    """Load task state from file."""
    if not STATE_FILE.exists():
        return {'tasks': {}, 'next_id': 1}

    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {'tasks': {}, 'next_id': 1}


def save_state(state: Dict[str, Any]):
    """Save task state to file."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2, default=str)


def generate_task_id(state: Dict[str, Any]) -> str:
    """Generate a new task ID."""
    task_id = f"ralph_{state['next_id']:04d}"
    state['next_id'] += 1
    return task_id


def run_task(command: str, name: str, timeout: int = DEFAULT_TIMEOUT) -> Dict[str, Any]:
    """
    Start a background task.

    Args:
        command: Shell command to run
        name: Human-readable task name
        timeout: Timeout in seconds (0 for no timeout)

    Returns:
        Task info dict
    """
    state = load_state()
    task_id = generate_task_id(state)

    # Create output file
    output_dir = Path('/tmp/ralph')
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{task_id}.log"

    # Start process
    with open(output_file, 'w') as out:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=out,
            stderr=subprocess.STDOUT,
            cwd=config_loader.ROOT_PATH,
            start_new_session=True  # Detach from parent
        )

    task = {
        'id': task_id,
        'name': name,
        'command': command,
        'pid': process.pid,
        'status': 'running',
        'started_at': datetime.now().isoformat(),
        'timeout': timeout,
        'output_file': str(output_file),
        'exit_code': None,
        'completed_at': None,
    }

    state['tasks'][task_id] = task
    save_state(state)

    return task


def check_task(task_id: str) -> Optional[Dict[str, Any]]:
    """Check status of a task and update if completed."""
    state = load_state()
    task = state['tasks'].get(task_id)

    if not task:
        return None

    if task['status'] == 'running':
        # Check if process is still running
        try:
            os.kill(task['pid'], 0)  # Signal 0 = check existence
        except OSError:
            # Process completed
            task['status'] = 'completed'
            task['completed_at'] = datetime.now().isoformat()

            # Try to get exit code (may not be available for detached processes)
            try:
                _, status = os.waitpid(task['pid'], os.WNOHANG)
                task['exit_code'] = os.WEXITSTATUS(status) if os.WIFEXITED(status) else -1
            except ChildProcessError:
                task['exit_code'] = 0  # Assume success if we can't check

            save_state(state)

    return task


def get_task_output(task_id: str, tail: int = 50) -> str:
    """Get recent output from a task."""
    state = load_state()
    task = state['tasks'].get(task_id)

    if not task:
        return f"Task {task_id} not found"

    output_file = Path(task['output_file'])
    if not output_file.exists():
        return "No output file found"

    try:
        with open(output_file, 'r') as f:
            lines = f.readlines()
            if tail > 0:
                lines = lines[-tail:]
            return ''.join(lines)
    except IOError as e:
        return f"Error reading output: {e}"


def kill_task(task_id: str) -> bool:
    """Kill a running task."""
    state = load_state()
    task = state['tasks'].get(task_id)

    if not task:
        return False

    if task['status'] != 'running':
        return False

    try:
        # Kill process group
        os.killpg(os.getpgid(task['pid']), signal.SIGTERM)
        time.sleep(0.5)

        # Force kill if still running
        try:
            os.kill(task['pid'], 0)
            os.killpg(os.getpgid(task['pid']), signal.SIGKILL)
        except OSError:
            pass

        task['status'] = 'killed'
        task['completed_at'] = datetime.now().isoformat()
        save_state(state)
        return True

    except OSError:
        return False


def list_tasks(show_all: bool = False) -> List[Dict[str, Any]]:
    """List all tasks."""
    state = load_state()
    tasks = list(state['tasks'].values())

    # Update status of running tasks
    for task in tasks:
        if task['status'] == 'running':
            check_task(task['id'])

    # Reload after updates
    state = load_state()
    tasks = list(state['tasks'].values())

    if not show_all:
        # Filter to recent tasks (last 24 hours) or running
        cutoff = datetime.now().timestamp() - 86400
        tasks = [
            t for t in tasks
            if t['status'] == 'running' or
               datetime.fromisoformat(t['started_at']).timestamp() > cutoff
        ]

    return sorted(tasks, key=lambda t: t['started_at'], reverse=True)


def clean_tasks(keep_running: bool = True) -> int:
    """Clean completed tasks from state."""
    state = load_state()
    original_count = len(state['tasks'])

    if keep_running:
        state['tasks'] = {
            tid: task for tid, task in state['tasks'].items()
            if task['status'] == 'running'
        }
    else:
        state['tasks'] = {}

    save_state(state)

    # Clean up output files
    output_dir = Path('/tmp/ralph')
    if output_dir.exists():
        for f in output_dir.glob('ralph_*.log'):
            task_id = f.stem
            if task_id not in state['tasks']:
                f.unlink()

    return original_count - len(state['tasks'])


def format_status(tasks: List[Dict[str, Any]]) -> str:
    """Format task list for display."""
    if not tasks:
        return "No tasks found."

    lines = []
    lines.append("=" * 60)
    lines.append("RALPH TASK STATUS")
    lines.append("=" * 60)

    for task in tasks:
        status_icon = {
            'running': '🔄',
            'completed': '✅',
            'failed': '❌',
            'killed': '🛑',
        }.get(task['status'], '❓')

        lines.append(f"\n{status_icon} [{task['id']}] {task['name']}")
        lines.append(f"   Command: {task['command'][:50]}...")
        lines.append(f"   Status:  {task['status']}")
        lines.append(f"   Started: {task['started_at']}")

        if task['completed_at']:
            lines.append(f"   Completed: {task['completed_at']}")
        if task['exit_code'] is not None:
            lines.append(f"   Exit Code: {task['exit_code']}")

        lines.append(f"   Output:  {task['output_file']}")

    lines.append("\n" + "=" * 60)
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Ralph - Long-running task manager')
    parser.add_argument('--status', action='store_true', help='Show task status')
    parser.add_argument('--all', action='store_true', help='Show all tasks (with --status)')
    parser.add_argument('--run', type=str, help='Command to run')
    parser.add_argument('--name', type=str, default='task', help='Task name')
    parser.add_argument('--timeout', type=int, default=DEFAULT_TIMEOUT, help='Timeout in seconds')
    parser.add_argument('--check', type=str, help='Check specific task ID')
    parser.add_argument('--output', type=str, help='Get output from task ID')
    parser.add_argument('--tail', type=int, default=50, help='Lines of output to show')
    parser.add_argument('--kill', type=str, help='Kill task by ID')
    parser.add_argument('--clean', action='store_true', help='Clean completed tasks')

    args = parser.parse_args()

    if args.status:
        tasks = list_tasks(show_all=args.all)
        print(format_status(tasks))

    elif args.run:
        task = run_task(args.run, args.name, args.timeout)
        print(f"Started task: {task['id']}")
        print(f"  Name: {task['name']}")
        print(f"  PID: {task['pid']}")
        print(f"  Output: {task['output_file']}")

    elif args.check:
        task = check_task(args.check)
        if task:
            print(format_status([task]))
        else:
            print(f"Task {args.check} not found")

    elif args.output:
        output = get_task_output(args.output, args.tail)
        print(output)

    elif args.kill:
        if kill_task(args.kill):
            print(f"Killed task {args.kill}")
        else:
            print(f"Could not kill task {args.kill}")

    elif args.clean:
        cleaned = clean_tasks()
        print(f"Cleaned {cleaned} completed tasks")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
