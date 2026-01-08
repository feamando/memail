# Commit - Create Git Commit

Create a well-formatted git commit for staged changes.

## Instructions

### Step 1: Check Status

```bash
git status
git diff --cached
```

Verify there are staged changes to commit.

### Step 2: Review Changes

Analyze staged changes:
- What files are modified?
- What's the nature of the change? (feat, fix, refactor, docs, test)
- Is it a single logical change or multiple?

### Step 3: Check Recent Commits

```bash
git log --oneline -5
```

Follow the existing commit message style.

### Step 4: Create Commit

Use conventional commit format:

```
<type>: <short description>

<optional longer description>

Co-Authored-By: Gemini <noreply@google.com>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code restructuring
- `docs`: Documentation
- `test`: Test changes
- `chore`: Maintenance

### Step 5: Verify

```bash
git log -1
git status
```

Confirm commit was created successfully.

## Execute

Review staged changes and create an appropriate commit.
