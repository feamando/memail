# Boot - Initialize Development Session

Load project context and prepare for development work.

## Instructions

### Step 1: Load Core Context

Read the following files to establish context:

1. **CLAUDE.md** - Project entry point and overview
2. **AI_Guidance/Rules/AGENT_DEV_GUIDE.md** - Development guidelines
3. **AI_Guidance/Rules/CODING_STANDARDS.md** - Code style guide

### Step 2: Check Git Status

```bash
git status
git log --oneline -5
```

Understand current branch, pending changes, and recent history.

### Step 3: Load Brain Context

Read any existing Brain files:
- `AI_Guidance/Brain/Technical/patterns.md` - Project patterns
- `AI_Guidance/Brain/Technical/conventions.md` - Project conventions
- `AI_Guidance/Brain/Architecture/decisions/*.md` - ADRs

### Step 4: Check for Running Tasks

Check if Ralph has any running tasks:

```bash
python3 AI_Guidance/Tools/ralph_manager.py --status
```

### Step 5: Confirm Ready

Report:
- Current branch and status
- Any pending changes
- Running tasks (if any)
- Ready for development

## Execute

Run the boot sequence now.
