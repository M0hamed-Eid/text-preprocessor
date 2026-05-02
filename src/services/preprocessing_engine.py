import re

from src.services.english_service import preprocess_english_text
from src.services.arabic_service import preprocess_arabic_text


def detect_text_language(text: str) -> str:
    """
    Basic language detection:
    Detect Arabic characters; otherwise assume English.
    """
    arabic_pattern = re.compile(r'[\u0600-\u06FF]')
    
    if arabic_pattern.search(text):
        return "arabic"
    
    return "english"


def preprocess_text(request_data) -> dict:
    """
    Unified preprocessing pipeline.
    """

    detected_language = detect_text_language(request_data.text)

    # Language mismatch handling
    if detected_language != request_data.language:
        raise ValueError(
            f"Language mismatch detected. Input appears to be '{detected_language}' "
            f"but '{request_data.language}' was selected."
        )

    # Route processing
    if request_data.language == "english":
        processed_text = preprocess_english_text(
            text=request_data.text,
            remove_stopwords=request_data.remove_stopwords,
            stemming=request_data.stemming,
            lemmatization=request_data.lemmatization,
            normalization=request_data.normalization
        )

    elif request_data.language == "arabic":
        processed_text = preprocess_arabic_text(
            text=request_data.text,
            remove_stopwords=request_data.remove_stopwords,
            stemming=request_data.stemming,
            lemmatization=request_data.lemmatization,
            normalization=request_data.normalization
        )

    else:
        raise ValueError("Unsupported language.")

    return {
        "original_text": request_data.text,
        "processed_text": processed_text,
        "language": request_data.language,
        "applied_steps": {
            "remove_stopwords": request_data.remove_stopwords,
            "stemming": request_data.stemming,
            "lemmatization": request_data.lemmatization,
            "normalization": request_data.normalization
        }
    }