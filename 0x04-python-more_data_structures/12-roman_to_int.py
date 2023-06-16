#!/usr/bin/python3
def roman_to_int(roman_string):
    """ converts a Roman numeral to an integer."""
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return (0)

    number = len(roman_string)
    value_int = roman_dict[roman_string[number-1]]
    for char in range(number - 1, 0, -1):
        current_value = roman_dict[roman_string[char]]
        previous_value = roman_dict[roman_string[char-1]]

        if previous_value >= current_value:
            value_int += previous_value
        else:
            value_int -= previous_value

    return (value_int)
