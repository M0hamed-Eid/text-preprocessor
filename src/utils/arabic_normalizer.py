import re
from src.config.constants import (
    ARABIC_CLEANING_REGEX,
    ARABIC_NORMALIZATION_MAP,
    ARABIC_TASHKEEL_REGEX,
    ARABIC_TATWEEL
)


def remove_tashkeel(text: str) -> str:
    """
    Remove Arabic diacritics (Tashkeel).
    """
    return ARABIC_TASHKEEL_REGEX.sub("", text)


def remove_tatweel(text: str) -> str:
    """
    Remove Tatweel character.
    """
    return text.replace(ARABIC_TATWEEL, "")


def normalize_arabic_letters(text: str) -> str:
    """
    Normalize Arabic Alef/Hamza variations.
    """
    for original, replacement in ARABIC_NORMALIZATION_MAP.items():
        text = text.replace(original, replacement)
    return text


def clean_arabic_text(text: str) -> str:
    """
    Remove punctuation, numbers, and unwanted characters.
    """
    text = ARABIC_CLEANING_REGEX.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_arabic_text(text: str) -> str:
    """
    Full Arabic normalization pipeline.
    """
    text = remove_tashkeel(text)
    text = remove_tatweel(text)
    text = normalize_arabic_letters(text)
    text = clean_arabic_text(text)
    return text