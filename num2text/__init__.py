from .converter import convert_number
from .fa import number_to_farsi_words, is_supported_fa
from .en import number_to_english_words, is_supported_en

__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "MIT"

__all__ = [
    "convert_number",
    "number_to_farsi_words",
    "number_to_english_words",
    "is_supported_fa",
    "is_supported_en",
    "to_words",
    "is_supported_language",
]

def to_words(number, lang="en"):
    """
    Convert a number to its word representation in the specified language.

    Args:
        number (int or float): The number to convert.
        lang (str): Language code ('en' or 'fa').

    Returns:
        str: Word representation of the number.

    Raises:
        ValueError: If the language code is not supported.
    """
    return convert_number(number, lang)

def is_supported_language(lang):
    """
    Check if a given language code is supported.

    Args:
        lang (str): Language code to check.

    Returns:
        bool: True if supported, False otherwise.
    """
    return lang in ("en", "fa")
