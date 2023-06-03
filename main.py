from conversions import from_binary_to_decimal, from_decimal_to_binary
from exceptions import ConversionError

if __name__ == '__main__':
    binary_string = input("Enter a binary number: ")
    try:
        decimal_number = from_binary_to_decimal(value=binary_string)
        print(f"{binary_string}b = {decimal_number}d")
    except ConversionError as e:
        print(e)

    try:
        decimal_string = input("Enter an integer number: ")
        binary_number = from_decimal_to_binary(decimal_string)
        print(f"{decimal_string}d = {binary_number}b")
    except ConversionError as e:
        print(e)

'''
TO-DOs:
- Hexadecimal to binary
- Binary to hexadecimal
- Octal to binary
- Binary to octal
- Octal to decimal
- Decimal to octal
- Octal to hexadecimal
- Hexadecimal to octal
- Retrieve vendor name using https://macvendors.com/api
- Identify class based on IP address
- Calculate number of hosts based on slash notation or subnet mask
'''
