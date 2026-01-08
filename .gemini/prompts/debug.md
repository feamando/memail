# Debug - Debugging Assistance

Help diagnose and fix issues in the codebase.

## Arguments

- `<error>`: Error message or description
- `--file <path>`: Specific file to investigate
- `--trace`: Include stack trace analysis

## Instructions

### Step 1: Understand the Problem

- What error or unexpected behavior is occurring?
- When does it happen?
- What's the expected behavior?

### Step 2: Locate Relevant Code

Based on error message or file:
1. Find the source of the error
2. Trace the call stack
3. Identify related code

### Step 3: Analyze

Consider:
- Is the input valid?
- Are dependencies available?
- Is state correct at this point?
- Are there race conditions?
- Is error handling correct?

### Step 4: Propose Fix

1. Explain root cause
2. Propose minimal fix
3. Suggest how to prevent similar issues

### Step 5: Test Fix

If a fix is implemented:
```bash
pytest <relevant_test_file>
```

Or suggest manual verification steps.

## Execute

Analyze the provided error or issue and propose solutions.
