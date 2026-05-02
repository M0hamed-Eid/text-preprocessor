import re
from src.config.constants import ENGLISH_CLEANING_REGEX


def lowercase_text(text: str) -> str:
    """
    Convert text to lowercase.
    """
    return text.lower()


def clean_english_text(text: str) -> str:
    """
    Remove special characters, punctuation, and numbers from English text.
    """
    text = ENGLISH_CLEANING_REGEX.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokenize_text(text: str) -> list:
    """
    Split text into tokens.
    """
    return text.split()


def cleanup_tokens(tokens: list) -> list:
    """
    Remove empty or invalid tokens.
    """
    return [token.strip() for token in tokens if token.strip()]