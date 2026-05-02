from pydantic import BaseModel, Field, field_validator
from typing import Optional
from src.config.constants import SUPPORTED_LANGUAGES, DEFAULT_PREPROCESSING_OPTIONS

class PreprocessRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text to preprocess")
    
    language: str = Field(
        ...,
        description="Language of the input text (english or arabic)"
    )

    remove_stopwords: bool = DEFAULT_PREPROCESSING_OPTIONS["remove_stopwords"]
    stemming: bool = DEFAULT_PREPROCESSING_OPTIONS["stemming"]
    lemmatization: bool = DEFAULT_PREPROCESSING_OPTIONS["lemmatization"]
    normalization: bool = DEFAULT_PREPROCESSING_OPTIONS["normalization"]

    @field_validator("language")
    @classmethod
    def validate_language(cls, value):
        value = value.lower()
        if value not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Unsupported language. Supported languages are: {SUPPORTED_LANGUAGES}"
            )
        return value

    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Input text cannot be empty.")
        return value.strip()

class PreprocessResponse(BaseModel):
    original_text: str
    processed_text: str
    language: str
    applied_steps: dict
    success: bool = True
    message: Optional[str] = "Text preprocessing completed successfully."