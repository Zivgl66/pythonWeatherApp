def roman_to_decimal(roman_str):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "IL": 49, "IC": 99,
                  "ID": 499, "XL": 40, "XC": 90, "CD": 400}
    num = 0
    i = 0
    while i < len(roman_str):
        if i+1 < len(roman_str) and roman_str[i:i+2] in roman_dict:
            num += roman_dict[roman_str[i:i+2]]
            i += 2
        else:
            num += roman_dict[roman_str[i]]
            i += 1
    return num


def roman_to_decimal(roman_str):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    i = 0
    while i < len(roman_str):
        letter_1 = roman_dict[roman_str[i]]
        if i+1 < len(roman_str):
            letter_2 = roman_dict[roman_str[i + 1]]
            if letter_1 >= letter_2:
                num = num + letter_1
                i = i + 1
            else:
                num = num + letter_2 - letter_1
                i = i + 2
        else:
            num = num + letter_1
            i = i + 1
    return num


print(f"Roman to Decimal: {roman_to_decimal('XD')}")

