# Conversion Chart 1 and Chart 2
chart1 = {
    '00': '000', '01': '008', '02': '010', '03': '018', '04': '020', '05': '028', '06': '030', '07': '038',
    '08': '040', '09': '048', '10': '080', '11': '088', '12': '090', '13': '098', '14': '0A0', '15': '0A8',
    '16': '0B0', '17': '0B8', '18': '0C0', '19': '0C8', '20': '11D', '21': '115', '22': '10D', '23': '105',
    '24': '13D', '25': '135', '26': '12D', '27': '125', '28': '15D', '29': '155', '30': '19D', '31': '195',
    '32': '18D', '33': '185', '34': '1BD', '35': '1B5', '36': '1AD', '37': '1A5', '38': '1DD', '39': '1D5',
    '40': '23A', '41': '232', '42': '22A', '43': '222', '44': '21A', '45': '212', '46': '20A', '47': '202',
    '48': '27A', '49': '272', '50': '2BA', '51': '2B2', '52': '2AA', '53': '2A2', '54': '29A', '55': '292',
    '56': '28A', '57': '282', '58': '2FA', '59': '2F2', '60': '327', '61': '32F', '62': '337', '63': '33F',
    '64': '307', '65': '30F', '66': '317', '67': '31F', '68': '367', '69': '36F', '70': '3A7', '71': '3AF',
    '72': '3B7', '73': '3BF', '74': '387', '75': '38F', '76': '397', '77': '39F', '78': '3E7', '79': '3EF',
    '80': '474', '81': '47C', '82': '464', '83': '46C', '84': '454', '85': '45C', '86': '444', '87': '44C',
    '88': '434', '89': '43C', '90': '4F4', '91': '4FC', '92': '4E4', '93': '4EC', '94': '4D4', '95': '4DC',
    '96': '4C4', '97': '4CC', '98': '4B4', '99': '4BC'
}

chart2 = {
    '0': '00', '1': '08', '2': '10', '3': '18', '4': '20', '5': '28', '6': '30', '7': '38', '8': '40', '9': '48'
}

def hex_to_password(hex_code):
    # Step 1: Take the first three digits
    first_three = hex_code[:3]
    first_two_digits = None
    for key, value in chart1.items():
        if value.startswith(first_three):
            first_two_digits = key
            break
    
    if not first_two_digits:
        print("First part of the hex code does not match.")
        return
    
    # Step 3: Use the next two digits of the hex code and compare them with Chart 2
    second_part = int(hex_code[3:5], 16)  # Next two digits in hex
    closest_value = max([int(value, 16) for value in chart2.values() if int(value, 16) <= second_part])
    third_digit = list(chart2.values()).index(hex(closest_value)[2:].upper())

    # Step 4: Add two zeros to the right side of the value obtained in step 3
    hex_value_with_zeros = closest_value << 8  # Equivalent to multiplying by 100 in hex
    # Step 5: Subtract the number obtained in step 4 from the last four digits of the hex code
    last_four_digits = int(hex_code[3:], 16)
    hex_subtracted = last_four_digits - hex_value_with_zeros

    # Step 6: Use the result from step 5 and look up the last two digits in Chart 1
    last_two_digits = None
    for key, value in chart1.items():
        if value.lower() == hex(hex_subtracted)[2:].zfill(3).lower():
            last_two_digits = key
            break

    if last_two_digits is None:
        print("No match found in Chart 1 for the last digits.")
        return

    # Combine to form the final password
    password = first_two_digits + str(third_digit) + last_two_digits
    return password


# Example usage
hex_code = '4BC19B5'
password = hex_to_password(hex_code)
if password:
    print(f"The generated password for hex code {hex_code} is: {password}")
