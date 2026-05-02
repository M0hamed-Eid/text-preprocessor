from src.config.constants import ENGLISH_STOPWORDS, ARABIC_STOPWORDS, ENGLISH_CLEANING_REGEX

print("English Stopwords Sample:", list(ENGLISH_STOPWORDS)[:5])
print("Arabic Stopwords Sample:", list(ARABIC_STOPWORDS)[:5])
print("Regex Test:", ENGLISH_CLEANING_REGEX.sub("", "Hello!!! 123"))