from src.services.english_service import preprocess_english_text
from src.services.arabic_service import preprocess_arabic_text


# English Test
english_text = "Hello!!! Welcome to the world of AI and machine learning."
print("English Processed:")
print(preprocess_english_text(
    english_text,
    remove_stopwords=True,
    stemming=True
))


# Arabic Test
arabic_text = "السَّلامُ عَلَيْكُمْ ورحمةُ اللهِ وبركاتهـــ"
print("\nArabic Processed:")
print(preprocess_arabic_text(
    arabic_text,
    remove_stopwords=True,
    stemming=True
))