FA_NUMBERS = {
    0: "صفر",
    1: "یک",
    2: "دو",
    3: "سه",
    4: "چهار",
    5: "پنج",
    6: "شش",
    7: "هفت",
    8: "هشت",
    9: "نه",
    10: "ده",
    11: "یازده",
    12: "دوازده",
    13: "سیزده",
    14: "چهارده",
    15: "پانزده",
    16: "شانزده",
    17: "هفده",
    18: "هجده",
    19: "نوزده",
    20: "بیست",
    30: "سی",
    40: "چهل",
    50: "پنجاه",
    60: "شصت",
    70: "هفتاد",
    80: "هشتاد",
    90: "نود",
    100: "صد",
    200: "دویست",
    300: "سیصد",
    400: "چهارصد",
    500: "پانصد",
    600: "ششصد",
    700: "هفتصد",
    800: "هشتصد",
    900: "نهصد"
}

FA_BIG_UNITS = [
    (1_000_000_000, "میلیارد"),
    (1_000_000, "میلیون"),
    (1_000, "هزار")
]

def number_to_farsi_words(number):
    """
    Convert a number to its Persian (Farsi) word representation.
    Supports integers up to billions.

    Args:
        number (int): The number to convert.

    Returns:
        str: Farsi words.

    Raises:
        ValueError: If the number is not an integer.
    """
    if not isinstance(number, int):
        raise ValueError("Only integer values are supported for Persian conversion.")

    if number == 0:
        return FA_NUMBERS[0]

    if number < 0:
        return f"منفی {number_to_farsi_words(abs(number))}"

    parts = []
    
    for value, name in FA_BIG_UNITS:
        count = number // value
        if count:
            parts.append(f"{number_to_farsi_words(count)} {name}")
            number %= value

    if number >= 100:
        hundreds = (number // 100) * 100
        parts.append(FA_NUMBERS[hundreds])
        number %= 100

    if number in FA_NUMBERS and number != 0:
        parts.append(FA_NUMBERS[number])
    elif number:
        tens = (number // 10) * 10
        ones = number % 10
        if tens:
            parts.append(FA_NUMBERS[tens])
        if ones:
            parts.append(FA_NUMBERS[ones])

    return " و ".join(parts)

def is_supported_fa():
    """Check if Persian conversion is available."""
    return True
