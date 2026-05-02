from src.models.request_models import PreprocessRequest

sample_request = PreprocessRequest(
    text="Hello World!",
    language="english"
)

print(sample_request)

sample_request = PreprocessRequest(
    text="",
    language="french"
)

print(sample_request)