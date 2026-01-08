# CLAUDE.md - Memail Agent Entry Point

## Project Overview

**Memail** is a [describe project purpose here]. This repository uses an AI-assisted development workflow with Claude Code.

## Quick Start

```bash
# Boot the agent (loads context and checks setup)
/boot

# Check long-running task status
/ralph-status
```

## Agent Guidelines

### Code Quality
- Write clean, maintainable code following `AI_Guidance/Rules/CODING_STANDARDS.md`
- Include tests for new functionality
- Document public APIs and complex logic

### Git Workflow
- Use conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`
- Keep commits atomic and focused
- Run tests before committing

### Development Process
1. Understand the task fully before writing code
2. Plan the approach (use `/adr` for significant decisions)
3. Implement with tests
4. Review with `/review` or `/orthogonal`
5. Commit with `/commit`

## Key Commands

| Command | Purpose |
|---------|---------|
| `/boot` | Initialize agent context |
| `/commit` | Create well-formatted git commit |
| `/review` | Code review current changes |
| `/test` | Run test suite |
| `/debug` | Debugging assistance |
| `/refactor` | Suggest refactoring improvements |
| `/adr` | Create Architecture Decision Record |
| `/ralph-status` | Check long-running tasks |
| `/ralph-run` | Start long-running task |
| `/orthogonal` | Devil's advocate review |

## Project Structure

```
memail/
├── .claude/              # Claude Code configuration
│   ├── commands/         # Slash commands (/command)
│   └── settings.json     # Project settings
├── .gemini/              # Gemini Code Assist configuration
│   ├── prompts/          # Custom prompts (@command)
│   └── settings.json     # Project settings
├── AI_Guidance/          # Agent guidance (shared)
│   ├── Rules/            # Coding standards, agent guides
│   ├── Tools/            # Python utilities
│   └── Brain/            # Knowledge base
│       ├── Architecture/ # ADRs and technical decisions
│       └── Technical/    # Patterns, conventions
├── src/                  # Source code (TBD)
├── tests/                # Test files (TBD)
├── config.yaml           # Project configuration
├── CLAUDE.md             # Claude entry point
└── GEMINI.md             # Gemini entry point
```

## Configuration

See `config.yaml` for project-specific settings including:
- API keys (Gemini, etc.)
- Path configurations
- Project metadata

## Brain Knowledge Base

The `AI_Guidance/Brain/` directory stores project knowledge:

- **Architecture/decisions/** - ADRs for significant technical decisions
- **Technical/patterns.md** - Code patterns used in this project
- **Technical/conventions.md** - Naming conventions, file organization

## For More Information

- `AI_Guidance/Rules/CODING_STANDARDS.md` - Code style guide
- `AI_Guidance/Rules/AGENT_DEV_GUIDE.md` - How the agent should approach development
