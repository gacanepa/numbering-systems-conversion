from exceptions import ConversionError
from valid_characters import BINARY_CHARACTERS


def from_binary_to_decimal(value: str) -> int:
    if not isinstance(value, str):
        raise TypeError(f"{value} is not a string")
    if not all([character in BINARY_CHARACTERS for character in value]):
        raise ConversionError(f"{value} contains non-binary characters")
    characters = list(value)
    result = 0
    for index, character in enumerate(characters):
        result += int(character) * 2 ** (len(characters) - int(index) - 1)

    return result
