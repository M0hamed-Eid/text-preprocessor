from src.utils.text_cleaner import lowercase_text, clean_english_text
from src.utils.arabic_normalizer import normalize_arabic_text


# English Test
english_text = "Hello!!! Welcome to AI 2026."
print("Lowercase:", lowercase_text(english_text))
print("Cleaned:", clean_english_text(english_text))


# Arabic Test
arabic_text = "السَّلامُ عَلَيْكُمْ ورحمةُ اللهِ وبركاتهـــ"
print("Normalized Arabic:", normalize_arabic_text(arabic_text))