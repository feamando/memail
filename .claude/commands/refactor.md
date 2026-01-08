# Refactor - Code Refactoring Suggestions

Analyze code and suggest refactoring improvements.

## Arguments

- `<file>`: File to analyze
- `--function <name>`: Specific function to refactor
- `--pattern <pattern>`: Apply specific pattern (extract, inline, rename)

## Instructions

### Step 1: Read Code

Read the target file or function to understand current structure.

### Step 2: Identify Issues

Look for:
- **Long functions** (> 50 lines)
- **Deep nesting** (> 3 levels)
- **Duplicate code**
- **Poor naming**
- **Mixed responsibilities**
- **Complex conditionals**
- **Magic numbers/strings**

### Step 3: Suggest Improvements

For each issue, suggest specific refactoring:

| Issue | Refactoring |
|-------|-------------|
| Long function | Extract method |
| Duplicate code | Extract shared function |
| Complex conditional | Replace with guard clauses or strategy |
| Magic values | Extract to constants |
| Mixed responsibilities | Split into separate modules |

### Step 4: Implement (if requested)

If user approves:
1. Make changes incrementally
2. Run tests after each change
3. Keep changes minimal and focused

### Safety

- Don't change public interfaces without discussion
- Run tests after refactoring
- Commit refactoring separately from features

## Execute

Analyze the target code and propose refactoring.
