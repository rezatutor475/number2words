EN_NUMBERS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred"
}

EN_BIG_UNITS = [
    (1_000_000_000, "billion"),
    (1_000_000, "million"),
    (1_000, "thousand")
]

def number_to_english_words(number):
    """
    Convert an integer number to its English word representation.

    Args:
        number (int): The number to convert.

    Returns:
        str: English words.

    Raises:
        ValueError: If input is not an integer.
    """
    if not isinstance(number, int):
        raise ValueError("Only integer values are supported for English conversion.")

    if number == 0:
        return EN_NUMBERS[0]

    if number < 0:
        return f"minus {number_to_english_words(abs(number))}"

    parts = []

    for value, name in EN_BIG_UNITS:
        count = number // value
        if count:
            parts.append(f"{number_to_english_words(count)} {name}")
            number %= value

    if number >= 100:
        hundreds = number // 100
        parts.append(f"{EN_NUMBERS[hundreds]} hundred")
        number %= 100

    if number in EN_NUMBERS and number != 0:
        parts.append(EN_NUMBERS[number])
    elif number:
        tens = (number // 10) * 10
        ones = number % 10
        if tens:
            parts.append(EN_NUMBERS[tens])
        if ones:
            parts.append(EN_NUMBERS[ones])

    return " ".join(parts)

def is_supported_en():
    """Check if English conversion is available."""
    return True
