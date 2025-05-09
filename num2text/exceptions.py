class NumberConversionError(Exception):
    """Base exception for number conversion errors."""
    pass


class UnsupportedLanguageError(NumberConversionError):
    """Raised when an unsupported language is requested."""
    def __init__(self, lang):
        message = f"Unsupported language code: '{lang}'"
        super().__init__(message)
        self.lang = lang


class InvalidNumberError(NumberConversionError):
    """Raised when input is not a valid number."""
    def __init__(self, value):
        message = f"Invalid number input: {value}"
        super().__init__(message)
        self.value = value


class NumberOutOfRangeError(NumberConversionError):
    """Raised when a number is out of the supported conversion range."""
    def __init__(self, number, lang):
        message = f"Number '{number}' is out of range for language '{lang}'"
        super().__init__(message)
        self.number = number
        self.lang = lang


class LanguageNotImplementedError(NumberConversionError):
    """Raised when a language is recognized but not yet implemented."""
    def __init__(self, lang):
        message = f"Language '{lang}' is recognized but not yet implemented."
        super().__init__(message)
        self.lang = lang
