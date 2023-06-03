from collections import deque
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


def from_decimal_to_binary(value: str) -> str:
    if not value.isdigit():
        raise TypeError(f"{value} is not an integer number")
    rest_value = int(value)
    # The problem domain does not require converting negative numbers
    if rest_value < 0:
        raise TypeError(f"{value} should be an integer greater than 0")
    if rest_value in [0, 1]:
        return value
    # Use a deque to append items to the left for performance reasons
    result = deque([])
    while rest_value > 1:
        rest_value, remainder = divmod(rest_value, 2)
        result.appendleft(str(remainder))
    # Append the last remainder (less significant bit) once outside the loop
    result.appendleft(str(remainder))

    return "".join(result)
