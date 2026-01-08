# Conventions

Project-specific conventions for memail.

## File Naming

### Python Files
- Modules: `snake_case.py` (e.g., `email_parser.py`)
- Test files: `test_<module>.py` (e.g., `test_email_parser.py`)
- Config: `config.py`, `settings.py`

### Directories
- Lowercase with underscores: `email_handlers/`
- Test directories mirror source: `src/services/` → `tests/services/`

## Directory Structure

```
memail/
├── src/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration
│   ├── models/              # Data models
│   │   ├── __init__.py
│   │   └── email.py
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   ├── fetcher.py
│   │   └── parser.py
│   ├── api/                 # API endpoints (if applicable)
│   │   ├── __init__.py
│   │   └── routes.py
│   └── utils/               # Shared utilities
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── test_models/
│   └── test_services/
├── AI_Guidance/             # Agent guidance
│   ├── Brain/               # Knowledge base
│   ├── Rules/               # Agent rules
│   └── Tools/               # Agent tools
├── config.yaml              # Project config
├── pyproject.toml           # Project metadata
└── CLAUDE.md                # Agent entry point
```

## API Design

### REST Endpoints
```
GET    /emails          # List emails
GET    /emails/{id}     # Get single email
POST   /emails          # Create email (send)
PUT    /emails/{id}     # Update email
DELETE /emails/{id}     # Delete email
```

### Response Format
```python
{
    "data": {...},        # Main response data
    "meta": {             # Metadata
        "total": 100,
        "page": 1
    },
    "errors": []          # List of errors (if any)
}
```

## Database Schema (if applicable)

### Table Naming
- Plural nouns: `emails`, `users`, `attachments`
- Join tables: `email_labels`

### Column Naming
- Snake case: `created_at`, `email_id`
- Foreign keys: `<table>_id` (e.g., `user_id`)
- Timestamps: `created_at`, `updated_at`, `deleted_at`

### Index Naming
- `ix_<table>_<column>` for single column
- `ix_<table>_<col1>_<col2>` for composite

## Git Conventions

### Branch Names
```
feat/<description>      # New feature
fix/<description>       # Bug fix
refactor/<description>  # Refactoring
docs/<description>      # Documentation
test/<description>      # Tests
chore/<description>     # Maintenance
```

### Commit Messages
Follow conventional commits:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Code Organization

### Imports Order
1. Standard library
2. Third-party packages
3. Local imports

Each group alphabetically sorted.

### Module Structure
```python
"""Module docstring."""

# Imports
import os
from typing import List

# Constants
DEFAULT_VALUE = 10

# Exceptions
class CustomError(Exception):
    pass

# Classes
class MyClass:
    pass

# Functions
def my_function():
    pass

# Main
if __name__ == "__main__":
    main()
```

## Versioning

Use semantic versioning: `MAJOR.MINOR.PATCH`

- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)
