# Ralph Status - Check Background Tasks

Check status of long-running background tasks.

## Instructions

### Step 1: Get Status

```bash
python3 AI_Guidance/Tools/ralph_manager.py --status
```

### Step 2: Report

For each task show:
- Task ID
- Name
- Status (running/completed/failed/killed)
- Start time
- Output file location

### Step 3: If Tasks Completed

For completed tasks, offer to show output:

```bash
python3 AI_Guidance/Tools/ralph_manager.py --output <task_id> --tail 50
```

### Step 4: Cleanup (optional)

If many old tasks, suggest cleanup:

```bash
python3 AI_Guidance/Tools/ralph_manager.py --clean
```

## Execute

Check Ralph task status now.
