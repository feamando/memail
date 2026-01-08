# Brain - Project Knowledge Base

This directory stores persistent knowledge about the memail project.

## Structure

```
Brain/
├── Architecture/
│   └── decisions/     # Architecture Decision Records (ADRs)
└── Technical/
    ├── patterns.md    # Code patterns used in this project
    └── conventions.md # Naming and structural conventions
```

## Architecture Decision Records (ADRs)

ADRs document significant technical decisions. Use the `/adr` command to create new ones.

### ADR Template
```markdown
# ADR-NNN: Title

## Status
Proposed | Accepted | Deprecated | Superseded

## Context
What is the issue we're addressing?

## Decision
What are we going to do?

## Consequences
What are the results of this decision?
```

### Naming Convention
`NNN-brief-title.md` (e.g., `001-use-asyncio-for-email-fetching.md`)

## Technical Knowledge

### patterns.md
Document recurring code patterns:
- How we handle async operations
- Error handling patterns
- Testing patterns
- Configuration patterns

### conventions.md
Document project-specific conventions:
- File naming
- Directory structure
- API design patterns
- Database schema conventions

## Usage

### Reading
The agent reads Brain files for context when:
- Making architecture decisions
- Writing new code
- Reviewing existing code

### Writing
Update Brain files when:
- Making significant technical decisions (create ADR)
- Establishing new patterns
- Changing conventions

### Commands
- `/adr` - Create new Architecture Decision Record
- `/boot` - Load Brain context at start of session
