import argparse
import sys
from number2words import convert_number
from number2words.exceptions import InvalidNumberError, UnsupportedLanguageError, NumberOutOfRangeError

def main():
    parser = argparse.ArgumentParser(
        description="Convert a number to its word representation in English or Persian."
    )
    parser.add_argument(
        "number",
        help="The number to convert. Supports integer values only.",
        type=str
    )
    parser.add_argument(
        "--lang",
        help="Language for conversion. Options: en (English), fa (Persian).",
        default="en",
        choices=["en", "fa"]
    )
    parser.add_argument(
        "--verbose",
        help="Display detailed output.",
        action="store_true"
    )

    args = parser.parse_args()

    try:
        number = int(args.number)
        result = convert_number(number, args.lang)
        if args.verbose:
            print(f"Number: {number}\nLanguage: {args.lang}\nWords: {result}")
        else:
            print(result)
    except ValueError:
        print("Error: Provided value is not a valid integer.", file=sys.stderr)
        sys.exit(1)
    except InvalidNumberError as e:
        print(f"InvalidNumberError: {e}", file=sys.stderr)
        sys.exit(2)
    except UnsupportedLanguageError as e:
        print(f"UnsupportedLanguageError: {e}", file=sys.stderr)
        sys.exit(3)
    except NumberOutOfRangeError as e:
        print(f"NumberOutOfRangeError: {e}", file=sys.stderr)
        sys.exit(4)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(99)

if __name__ == "__main__":
    main()
