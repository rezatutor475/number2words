import pytest
from number2words.en import number_to_english_words
from number2words.exceptions import InvalidNumberError

def test_single_digits():
    assert number_to_english_words(0) == "zero"
    assert number_to_english_words(5) == "five"

def test_teens():
    assert number_to_english_words(11) == "eleven"
    assert number_to_english_words(19) == "nineteen"

def test_tens():
    assert number_to_english_words(20) == "twenty"
    assert number_to_english_words(42) == "forty two"

def test_hundreds():
    assert number_to_english_words(100) == "one hundred"
    assert number_to_english_words(215) == "two hundred fifteen"

def test_thousands():
    assert number_to_english_words(1000) == "one thousand"
    assert number_to_english_words(2023) == "two thousand twenty three"

def test_millions():
    assert number_to_english_words(1_000_000) == "one million"
    assert number_to_english_words(2_300_100) == "two million three hundred thousand one hundred"

def test_billions():
    assert number_to_english_words(1_000_000_000) == "one billion"
    assert number_to_english_words(1_000_000_001) == "one billion one"

def test_negative():
    assert number_to_english_words(-7) == "minus seven"

def test_invalid_input():
    with pytest.raises(ValueError):
        number_to_english_words("12")

    with pytest.raises(ValueError):
        number_to_english_words(45.67)
