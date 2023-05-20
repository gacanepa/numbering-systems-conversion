class BinaryToDecimalError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Error: {repr(self.value)}"
