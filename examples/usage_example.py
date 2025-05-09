from number2words import convert_number
from number2words.exceptions import UnsupportedLanguageError, InvalidNumberError, NumberOutOfRangeError

def main():
    examples = [
        (0, "en"),
        (15, "fa"),
        (123, "en"),
        (1005, "fa"),
        (1_000_000, "en"),
        (-42, "fa"),
        (1_000_000_000, "en"),
        (999_999_999, "fa"),
        ("not_a_number", "en"),
        (123, "de")  # unsupported language
    ]

    for num, lang in examples:
        print(f"\nInput: {num} | Language: {lang.upper()}")
        try:
            result = convert_number(num, lang)
            print(f"Output: {result}")
        except UnsupportedLanguageError as e:
            print(f"UnsupportedLanguageError: {e}")
        except InvalidNumberError as e:
            print(f"InvalidNumberError: {e}")
        except NumberOutOfRangeError as e:
            print(f"NumberOutOfRangeError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
