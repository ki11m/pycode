def decimal_to_binary(number, precision=4):
    binary = ""
    while precision > 0:
        number *= 2
        if number >= 1:
            binary += "1"
            number -= 1
        else:
            binary += "0"
        precision -= 1
    return "0." + binary

decimal_number = float(input())
binary_representation = decimal_to_binary(decimal_number)
print(binary_representation)
