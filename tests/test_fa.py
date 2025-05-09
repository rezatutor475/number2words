import pytest
from number2words.fa import number_to_farsi_words
from number2words.exceptions import InvalidNumberError, NumberOutOfRangeError

def test_single_digits():
    assert number_to_farsi_words(0) == "صفر"
    assert number_to_farsi_words(5) == "پنج"

def test_two_digits():
    assert number_to_farsi_words(21) == "بیست و یک"
    assert number_to_farsi_words(99) == "نود و نه"

def test_exact_tens():
    assert number_to_farsi_words(20) == "بیست"
    assert number_to_farsi_words(90) == "نود"

def test_teens():
    assert number_to_farsi_words(11) == "یازده"
    assert number_to_farsi_words(19) == "نوزده"

def test_hundreds():
    assert number_to_farsi_words(100) == "صد"
    assert number_to_farsi_words(215) == "دویست و پانزده"

def test_thousands():
    assert number_to_farsi_words(1000) == "یک هزار"
    assert number_to_farsi_words(2023) == "دو هزار و بیست و سه"
    assert number_to_farsi_words(13_000) == "سیزده هزار"

def test_millions():
    assert number_to_farsi_words(1_000_000) == "یک میلیون"
    assert number_to_farsi_words(1_200_001) == "یک میلیون و دویست هزار و یک"

def test_billions():
    assert number_to_farsi_words(1_000_000_000) == "یک میلیارد"
    assert number_to_farsi_words(1_000_001_001) == "یک میلیارد و یک هزار و یک"

def test_negative_numbers():
    assert number_to_farsi_words(-15) == "منفی پانزده"
    assert number_to_farsi_words(-1_000_001) == "منفی یک میلیون و یک"

def test_invalid_input():
    with pytest.raises(ValueError):
        number_to_farsi_words("123")

    with pytest.raises(ValueError):
        number_to_farsi_words(12.5)

    with pytest.raises(ValueError):
        number_to_farsi_words(None)
