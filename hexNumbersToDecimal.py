hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    decimal = 0
    for digit in hexNum:
        if digit.upper() not in hexNumbers:
            return None
        decimal_value = hexNumbers[digit.upper()]
        decimal = decimal * 16 + decimal_value
    return decimal


value= input('Number HEX that you want to convert to decmal:')
print("Hex to Decimal: ", hexToDec(value))  

