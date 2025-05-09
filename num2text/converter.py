from .fa import number_to_farsi_words, is_supported_fa
from .en import number_to_english_words, is_supported_en

def convert_number(number, lang='en'):
    """
    Convert a number to words based on the selected language.

    Args:
        number (int or float): The number to convert.
        lang (str): Language code ('en' or 'fa').

    Returns:
        str: Word representation of the number.

    Raises:
        ValueError: If language code is unsupported or number type is invalid.
    """
    validate_input(number, lang)

    if lang == 'fa':
        return number_to_farsi_words(number)
    elif lang == 'en':
        return number_to_english_words(number)


def validate_input(number, lang):
    """
    Validate the input number and language code.

    Args:
        number (int or float): The number to validate.
        lang (str): Language code.

    Raises:
        ValueError: If validation fails.
    """
    if not isinstance(number, (int, float)):
        raise ValueError("Only integers and floats are supported.")

    if lang == 'fa' and not is_supported_fa():
        raise ValueError("Farsi language support is currently unavailable.")
    elif lang == 'en' and not is_supported_en():
        raise ValueError("English language support is currently unavailable.")
    elif lang not in ('fa', 'en'):
        raise ValueError(f"Unsupported language code: {lang}")
