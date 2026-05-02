from pathlib import Path
import re

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Stopword files
ENGLISH_STOPWORDS_FILE = BASE_DIR / "stopwords_en.txt"
ARABIC_STOPWORDS_FILE = BASE_DIR / "stopwords_ar.txt"

# Supported languages
SUPPORTED_LANGUAGES = ["english", "arabic"]

# Default preprocessing options
DEFAULT_PREPROCESSING_OPTIONS = {
    "remove_stopwords": True,
    "stemming": False,
    "lemmatization": False,
    "normalization": True,
    "remove_punctuation": True,
    "lowercase": True
}

# Regex patterns
ENGLISH_CLEANING_REGEX = re.compile(r"[^a-zA-Z\s]")
ARABIC_CLEANING_REGEX = re.compile(r"[^\u0600-\u06FF\s]")

# Arabic normalization mappings
ARABIC_NORMALIZATION_MAP = {
    "أ": "ا",
    "إ": "ا",
    "آ": "ا",
    "ى": "ي",
    "ؤ": "و",
    "ئ": "ي",
    "ة": "ه"
}

# Arabic diacritics (Tashkeel)
ARABIC_TASHKEEL_REGEX = re.compile(r"[\u0617-\u061A\u064B-\u0652]")

# Tatweel
ARABIC_TATWEEL = "ـ"

def load_stopwords(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return set(
            line.strip()
            for line in file
            if line.strip()
        )

ENGLISH_STOPWORDS = load_stopwords(ENGLISH_STOPWORDS_FILE)
ARABIC_STOPWORDS = load_stopwords(ARABIC_STOPWORDS_FILE)