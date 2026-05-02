from pyarabic.araby import tokenize
from nltk.stem.isri import ISRIStemmer

from src.config.constants import ARABIC_STOPWORDS
from src.utils.arabic_normalizer import normalize_arabic_text


stemmer = ISRIStemmer()


def remove_arabic_stopwords(tokens: list) -> list:
    """
    Intelligent Arabic stopword filtering.
    """
    return [
        token for token in tokens
        if token not in ARABIC_STOPWORDS and len(token) > 1
    ]


def preprocess_arabic_text(
    text: str,
    remove_stopwords: bool = True,
    stemming: bool = False,
    lemmatization: bool = False,
    normalization: bool = True
) -> str:

    # Arabic normalization
    if normalization:
        text = normalize_arabic_text(text)

    # Tokenization
    tokens = tokenize(text)

    # Stopword removal
    if remove_stopwords:
        tokens = remove_arabic_stopwords(tokens)

    # Stemming
    if stemming:
        tokens = [stemmer.stem(token) for token in tokens]

    # Basic placeholder for lemmatization
    # Advanced Arabic lemmatization can later use CAMeL Tools
    if lemmatization:
        tokens = tokens

    return " ".join(tokens)