from word2num_converter.languages import english, hindi, marathi

LANGUAGE_MAP = {
    'en': english.convert_eng_number_phrases_in_sentence,
    'hin': hindi.convert_hin_number_phrases_in_sentence,
    'mr': marathi.convert_mar_number_phrases_in_sentence,
}

def convert_word2num(text: str, lang: str = 'en') -> str:
    if lang not in LANGUAGE_MAP:
        raise ValueError(f"Unsupported language code: {lang}")
    return LANGUAGE_MAP[lang](text)


# --- word2num_converter/__init__.py ---
from .converter import convert_word2num
__all__ = ["convert_word2num"]
