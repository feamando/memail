# ADR - Create Architecture Decision Record

Document significant technical decisions.

## Arguments

- `<title>`: Brief title for the decision
- `--status <status>`: Proposed (default), Accepted, Deprecated, Superseded

## Instructions

### Step 1: Get Next ADR Number

```bash
ls AI_Guidance/Brain/Architecture/decisions/*.md 2>/dev/null | wc -l
```

Next number = count + 1, formatted as 3 digits (001, 002, etc.)

### Step 2: Gather Information

Ask user for (if not provided):
1. **Context**: What problem are we solving?
2. **Options considered**: What alternatives exist?
3. **Decision**: What did we choose and why?
4. **Consequences**: What are the tradeoffs?

### Step 3: Create ADR

Create file: `AI_Guidance/Brain/Architecture/decisions/NNN-<slug>.md`

```markdown
# ADR-NNN: <Title>

## Status

<Proposed|Accepted|Deprecated|Superseded>

## Context

<What is the issue we're addressing?>

## Options Considered

### Option 1: <Name>
- Pros: ...
- Cons: ...

### Option 2: <Name>
- Pros: ...
- Cons: ...

## Decision

<What we chose and why>

## Consequences

### Positive
- ...

### Negative
- ...

### Neutral
- ...
```

### Step 4: Confirm

Show the created ADR and confirm file location.

## Execute

Create an ADR based on the provided title and information.
