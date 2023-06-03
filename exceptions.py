class ConversionError(Exception):
    def __init__(self, value="the input value is not valid"):
        self.value = value

    def __str__(self):
        return f"Error: {self.value}"
