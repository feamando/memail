# Orthogonal - Devil's Advocate Review

Get critical analysis from Gemini as a devil's advocate.

## Arguments

- `--file <path>`: Review a specific file
- `--diff`: Review staged git changes
- `--adr <path>`: Challenge an ADR
- `--idea "<text>"`: Challenge an idea or proposal

## Instructions

### Step 1: Determine Mode

Based on arguments:
- File review: Analyze code for issues
- Diff review: Review proposed changes
- ADR challenge: Question architecture decisions
- Idea challenge: Find weaknesses in proposals

### Step 2: Run Orthogonal Challenge

```bash
python3 AI_Guidance/Tools/orthogonal_challenge.py [options]
```

Options:
- `--file <path>`: Code file to review
- `--diff`: Review staged changes
- `--adr <path>`: ADR file to challenge
- `--idea "<text>"`: Idea to challenge

### Step 3: Present Results

Show the Gemini analysis, which covers:

**For Code:**
- Security concerns
- Performance issues
- Maintainability risks
- Edge cases
- Alternative approaches

**For Diffs:**
- Breaking changes
- Security implications
- Testing gaps
- Risks

**For ADRs:**
- Assumptions to challenge
- Alternatives not considered
- Long-term implications
- Operational concerns

**For Ideas:**
- Core assumptions
- Why it might fail
- Hidden costs
- Prerequisites

### Step 4: Action Items

Based on the review, suggest:
1. Issues to address before proceeding
2. Questions to answer
3. Tests to add

## Execute

Run orthogonal challenge with the provided arguments.
