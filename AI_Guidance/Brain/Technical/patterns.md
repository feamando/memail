# Code Patterns

Recurring patterns used in the memail project.

## Async Operations

### Async Context Manager
```python
async with EmailClient() as client:
    messages = await client.fetch_messages()
```

### Async Generator
```python
async def stream_emails(query: str):
    async for batch in paginate(query):
        for email in batch:
            yield email
```

### Concurrent Tasks
```python
async def process_multiple(emails: List[Email]) -> List[Result]:
    tasks = [process_email(email) for email in emails]
    return await asyncio.gather(*tasks, return_exceptions=True)
```

## Error Handling

### Retry with Backoff
```python
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(NetworkError)
)
async def fetch_with_retry(url: str) -> Response:
    return await client.get(url)
```

### Result Pattern
```python
@dataclass
class Result(Generic[T]):
    value: Optional[T] = None
    error: Optional[Exception] = None

    @property
    def is_success(self) -> bool:
        return self.error is None
```

### Context-Rich Errors
```python
class EmailParseError(Exception):
    def __init__(self, message: str, email_id: str, raw_content: str = None):
        super().__init__(message)
        self.email_id = email_id
        self.raw_content = raw_content
```

## Configuration

### Pydantic Settings
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    email_host: str
    email_port: int = 993
    debug: bool = False

    class Config:
        env_file = ".env"
        env_prefix = "MEMAIL_"
```

### Configuration Hierarchy
```
1. Environment variables (highest priority)
2. .env file
3. config.yaml
4. Default values (lowest priority)
```

## Data Models

### Pydantic Models
```python
from pydantic import BaseModel, Field

class Email(BaseModel):
    id: str = Field(..., description="Unique email ID")
    subject: str
    body: str
    sent_at: datetime

    class Config:
        frozen = True  # Immutable
```

### Enum for Status
```python
from enum import Enum, auto

class EmailStatus(Enum):
    UNREAD = auto()
    READ = auto()
    ARCHIVED = auto()
    DELETED = auto()
```

## Testing

### Fixtures
```python
@pytest.fixture
def email_client(mocker):
    client = mocker.Mock(spec=EmailClient)
    client.fetch.return_value = [sample_email()]
    return client
```

### Async Tests
```python
@pytest.mark.asyncio
async def test_fetch_emails():
    async with EmailClient() as client:
        emails = await client.fetch()
        assert len(emails) > 0
```

### Parameterized Tests
```python
@pytest.mark.parametrize("input,expected", [
    ("valid@email.com", True),
    ("invalid", False),
    ("", False),
])
def test_validate_email(input, expected):
    assert validate_email(input) == expected
```

## Logging

### Structured Logging
```python
import structlog

logger = structlog.get_logger()

logger.info(
    "email_processed",
    email_id=email.id,
    duration_ms=elapsed,
    status="success"
)
```

### Log Context
```python
with structlog.contextvars.bound_contextvars(
    request_id=request_id,
    user_id=user_id
):
    process_request()  # All logs include request_id and user_id
```
