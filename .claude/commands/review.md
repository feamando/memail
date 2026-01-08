# Review - Code Review Current Changes

Review staged or unstaged changes for quality issues.

## Arguments

- No args: Review staged changes
- `--all`: Review all changes (staged + unstaged)
- `<file>`: Review specific file

## Instructions

### Step 1: Get Changes

Based on arguments:
- No args: `git diff --cached`
- `--all`: `git diff HEAD`
- File: Read the specific file

### Step 2: Quality Checklist

Review for:

**Correctness**
- Logic errors
- Edge cases not handled
- Potential null/undefined issues

**Security**
- Input validation
- Injection vulnerabilities
- Sensitive data exposure

**Performance**
- Unnecessary loops/iterations
- Missing caching opportunities
- Resource leaks

**Maintainability**
- Code clarity and readability
- Appropriate naming
- Function/method size
- Error handling

**Testing**
- Are tests included?
- Do tests cover edge cases?

### Step 3: Report

Structure review as:

```
## Summary
Brief overview of changes

## Issues Found
### Critical
- Issue description with file:line

### Suggestions
- Improvement suggestions

## Approval Status
APPROVED / NEEDS CHANGES
```

## Execute

Review the changes and provide feedback.
