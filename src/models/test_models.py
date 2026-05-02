from src.models.request_models import PreprocessRequest
from pydantic import ValidationError

sample_request = PreprocessRequest(
    text="Hello World!",
    language="english"
)

print(sample_request)

try:
    sample_request = PreprocessRequest(
        text="",
        language="french"
    )
    print(sample_request)
except ValidationError as e:
    print(f"Validation failed as expected!\nErrors: {e.json()}")