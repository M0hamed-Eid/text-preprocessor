from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

from src.config.constants import ENGLISH_STOPWORDS
from src.utils.text_cleaner import (
    lowercase_text,
    clean_english_text,
    cleanup_tokens
)


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def remove_english_stopwords(tokens: list) -> list:
    """
    Intelligent stopword removal while preserving meaningful content.
    """
    return [
        token for token in tokens
        if token.lower() not in ENGLISH_STOPWORDS and len(token) > 1
    ]


def preprocess_english_text(
    text: str,
    remove_stopwords: bool = True,
    stemming: bool = False,
    lemmatization: bool = False,
    normalization: bool = True
) -> str:

    # Normalization
    if normalization:
        text = lowercase_text(text)
        text = clean_english_text(text)

    # Tokenization
    tokens = word_tokenize(text)

    # Cleanup
    tokens = cleanup_tokens(tokens)

    # Stopword removal
    if remove_stopwords:
        tokens = remove_english_stopwords(tokens)

    # Lemmatization
    if lemmatization:
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Stemming
    if stemming:
        tokens = [stemmer.stem(token) for token in tokens]

    return " ".join(tokens)