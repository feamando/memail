# Agent Development Guide

Guidelines for how the AI agent should approach software development in this project.

## Core Principles

### 1. Understand Before Coding
- **Read first**: Always read existing code before modifying
- **Ask questions**: If requirements are unclear, ask before implementing
- **Check patterns**: Look for existing patterns in the codebase to follow

### 2. Quality Over Speed
- Write code that's easy to read and maintain
- Include appropriate tests
- Handle errors gracefully
- Document complex logic

### 3. Minimal Changes
- Make focused, atomic changes
- Don't refactor unrelated code
- Avoid scope creep
- One concern per commit

## Development Workflow

### Before Starting
1. Understand the task requirements fully
2. Check if similar functionality exists
3. Identify affected files and dependencies
4. Consider edge cases and error scenarios

### While Implementing
1. Follow existing code patterns
2. Write tests alongside implementation
3. Handle errors explicitly
4. Add comments for non-obvious logic

### After Implementing
1. Run tests (`/test`)
2. Review changes (`/review` or `/orthogonal`)
3. Format and lint code
4. Create meaningful commit (`/commit`)

## Code Quality Standards

### Readability
- Use descriptive variable and function names
- Keep functions focused and small (< 50 lines ideal)
- Prefer explicit over clever
- Use consistent formatting

### Error Handling
- Never silently swallow errors
- Use specific exception types
- Provide helpful error messages
- Log errors with context

### Testing
- Test public interfaces
- Cover edge cases
- Test error paths
- Keep tests focused and independent

### Documentation
- Document public APIs
- Explain "why" not "what"
- Keep docs near code
- Update docs with code changes

## Git Practices

### Commit Messages
Use conventional commits:
```
feat: Add email parsing functionality
fix: Handle empty subject lines
refactor: Extract validation logic
docs: Update API documentation
test: Add integration tests for parser
```

### Commit Scope
- One logical change per commit
- Tests with implementation (same commit)
- Refactoring in separate commits
- Don't mix formatting with logic changes

## When to Ask for Help

### Ask the User When:
- Requirements are ambiguous
- Multiple valid approaches exist
- Changes affect user-facing behavior
- Security implications are unclear

### Use `/orthogonal` When:
- Making architectural decisions
- Significant refactoring
- Adding new dependencies
- Security-sensitive changes

## Anti-Patterns to Avoid

### Don't Do This:
- Commit code that doesn't compile/run
- Skip tests for "simple" changes
- Copy-paste without understanding
- Ignore error handling
- Leave commented-out code
- Mix concerns in single commits

### Instead:
- Verify code works before committing
- Write tests for all changes
- Understand and adapt code to context
- Handle errors explicitly
- Delete unused code
- Make atomic, focused commits

## Tools Available

| Tool | Purpose |
|------|---------|
| `/test` | Run test suite |
| `/review` | Code review current changes |
| `/orthogonal` | Devil's advocate analysis |
| `/commit` | Create well-formatted commit |
| `/debug` | Debugging assistance |
| `/refactor` | Refactoring suggestions |
| `/adr` | Document architecture decisions |
| `/ralph-run` | Run long tasks in background |
| `/ralph-status` | Check background task status |

## Response Format

When completing development tasks, structure responses as:

1. **Understanding**: Brief restatement of the task
2. **Approach**: How you'll implement it
3. **Changes**: What files will be modified
4. **Implementation**: The actual code changes
5. **Testing**: How to verify the changes
6. **Next Steps**: Any follow-up needed
