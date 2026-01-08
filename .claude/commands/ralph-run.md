# Ralph Run - Start Background Task

Start a long-running task in the background.

## Arguments

- `<command>`: Command to run
- `--name <name>`: Task name (default: "task")
- `--timeout <seconds>`: Timeout in seconds (default: 300)

## Instructions

### Step 1: Validate Command

Ensure the command is appropriate for background execution:
- Test suites
- Builds
- Linting
- Long-running scripts

### Step 2: Start Task

```bash
python3 AI_Guidance/Tools/ralph_manager.py --run "<command>" --name "<name>" --timeout <timeout>
```

### Step 3: Report

Show:
- Task ID (for checking later)
- Output file location
- How to check status: `/ralph-status`

### Common Use Cases

```bash
# Run full test suite
/ralph-run "pytest" --name tests

# Run with coverage
/ralph-run "pytest --cov=src" --name coverage

# Run linting
/ralph-run "ruff check . && mypy ." --name lint

# Build project
/ralph-run "python setup.py build" --name build
```

## Execute

Start the background task with the provided command.
