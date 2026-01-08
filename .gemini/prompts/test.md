# Test - Run Test Suite

Run tests for the project.

## Arguments

- No args: Run full test suite
- `<path>`: Run specific test file or directory
- `--coverage`: Run with coverage report
- `--failed`: Re-run only failed tests

## Instructions

### Determine Test Scope

Based on arguments:
- No args: `pytest`
- Path provided: `pytest <path>`
- `--coverage`: `pytest --cov=src --cov-report=term-missing`
- `--failed`: `pytest --lf`

### Run Tests

For quick tests (< 2 minutes expected):
```bash
pytest [options]
```

For longer test runs, use Ralph:
```bash
python3 AI_Guidance/Tools/ralph_manager.py --run "pytest [options]" --name "test-suite"
```

### Report Results

After tests complete:
1. Show pass/fail summary
2. Highlight any failures with file:line references
3. If coverage requested, show uncovered areas

### If Tests Fail

1. Identify the failing test(s)
2. Show the failure message and traceback
3. Suggest potential fixes based on the error

## Execute

Run tests based on the provided arguments.
