# Coding Standards

Code style and conventions for the memail project.

## General Principles

1. **Clarity over cleverness** - Write code that's easy to understand
2. **Explicit over implicit** - Be clear about intentions
3. **DRY but not too DRY** - Avoid premature abstraction
4. **YAGNI** - Don't add features until needed

## Python Standards

### Style
- Follow PEP 8
- Use `black` for formatting
- Use `ruff` for linting
- Use `mypy` for type checking

### Naming Conventions
```python
# Variables and functions: snake_case
user_email = "test@example.com"
def send_email(recipient: str) -> bool:
    pass

# Classes: PascalCase
class EmailParser:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_ATTACHMENT_SIZE = 10 * 1024 * 1024

# Private: leading underscore
def _internal_helper():
    pass

class MyClass:
    def _private_method(self):
        pass
```

### Type Hints
```python
from typing import Optional, List, Dict

def process_email(
    subject: str,
    body: str,
    attachments: Optional[List[str]] = None
) -> Dict[str, str]:
    """Process an email and return metadata."""
    pass
```

### Docstrings
```python
def complex_function(param1: str, param2: int) -> bool:
    """
    Brief description of what this does.

    More detailed explanation if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When param1 is empty
    """
    pass
```

### Error Handling
```python
# Good: Specific exceptions with context
try:
    result = process_email(email)
except EmailParseError as e:
    logger.error(f"Failed to parse email {email.id}: {e}")
    raise
except NetworkError as e:
    logger.warning(f"Network issue, will retry: {e}")
    return retry_with_backoff(process_email, email)

# Bad: Catching everything
try:
    result = process_email(email)
except Exception:
    pass  # Never do this
```

### Imports
```python
# Standard library first
import os
import sys
from pathlib import Path
from typing import Optional

# Third-party second
import requests
from pydantic import BaseModel

# Local imports last
from .utils import helper
from ..config import settings
```

## File Organization

### Project Structure
```
memail/
├── src/
│   ├── __init__.py
│   ├── main.py           # Entry point
│   ├── models/           # Data models
│   │   ├── __init__.py
│   │   └── email.py
│   ├── services/         # Business logic
│   │   ├── __init__.py
│   │   └── parser.py
│   └── utils/            # Utilities
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py       # Pytest fixtures
│   ├── test_models/
│   └── test_services/
└── config.yaml
```

### Module Layout
```python
"""
Module docstring explaining purpose.
"""

# Imports (grouped as above)
import os
from typing import List

# Constants
DEFAULT_TIMEOUT = 30

# Classes
class MyClass:
    pass

# Functions
def my_function():
    pass

# Main block (if applicable)
if __name__ == "__main__":
    main()
```

## Testing Standards

### Test Structure
```python
# test_email_parser.py
import pytest
from src.services.parser import EmailParser

class TestEmailParser:
    """Tests for EmailParser."""

    def test_parse_simple_email(self):
        """Parser extracts subject from simple email."""
        parser = EmailParser()
        result = parser.parse("Subject: Hello\n\nBody")
        assert result.subject == "Hello"

    def test_parse_empty_email_raises(self):
        """Parser raises ValueError for empty input."""
        parser = EmailParser()
        with pytest.raises(ValueError, match="Empty email"):
            parser.parse("")

    @pytest.mark.parametrize("input,expected", [
        ("Subject: A", "A"),
        ("Subject: B", "B"),
    ])
    def test_parse_various_subjects(self, input, expected):
        """Parser handles various subject formats."""
        parser = EmailParser()
        assert parser.parse(input).subject == expected
```

### Test Naming
- `test_<function>_<scenario>` or `test_<function>_<expected_behavior>`
- Be descriptive: `test_parse_email_with_attachments_extracts_all`

### Fixtures
```python
# conftest.py
import pytest

@pytest.fixture
def sample_email():
    """Provide a sample email for testing."""
    return {
        "subject": "Test",
        "body": "Hello world",
        "sender": "test@example.com"
    }

@pytest.fixture
def email_parser():
    """Provide a configured EmailParser instance."""
    return EmailParser(strict_mode=True)
```

## Git Conventions

### Branch Names
```
feat/add-email-parsing
fix/handle-empty-subject
refactor/extract-validation
docs/api-documentation
```

### Commit Messages
```
feat: Add email parsing with attachment support

- Implement MIME parsing for attachments
- Add size validation for attachments
- Support common file types (pdf, doc, images)

Closes #123
```

## Code Review Checklist

Before submitting changes, verify:

- [ ] Code compiles/runs without errors
- [ ] Tests pass (`pytest`)
- [ ] New code has tests
- [ ] Code is formatted (`black .`)
- [ ] Linting passes (`ruff check .`)
- [ ] Type hints are correct (`mypy .`)
- [ ] No hardcoded secrets or credentials
- [ ] Error handling is appropriate
- [ ] Documentation is updated if needed
