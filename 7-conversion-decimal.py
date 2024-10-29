# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary

# Function to convert decimal to octal
def decimal_to_octal(decimal):
    octal = oct(decimal).replace("0o", "")
    return octal

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal).replace("0x", "")
    return hexadecimal

# Main program
if __name__ == "__main__":
    decimal = int(input("Enter a decimal number: "))

    binary = decimal_to_binary(decimal)
    print("Binary: " + binary)

    octal = decimal_to_octal(decimal)
    print("Octal: " + octal)

    hexadecimal = decimal_to_hexadecimal(decimal)
    print("Hexadecimal: " + hexadecimal)