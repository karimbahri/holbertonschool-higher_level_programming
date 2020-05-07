#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or str is None:
        return 0

    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                     'D': 500, 'M': 1000}
    integer = 0

    for i in range(len(roman_string) - 1, -1, -1):
        if roman_string[i] in roman_numbers.keys():
            if (roman_string[i - 1] in roman_numbers.keys() and
                i > 0 and roman_numbers[roman_string[i]] >
                    roman_numbers[roman_string[i - 1]]):
                        integer += (roman_numbers[roman_string[i]] -
                                    roman_numbers[roman_string[i - 1]])
                        i -= 2
                        if i <= 0:
                            break
            else:
                integer += roman_numbers[roman_string[i]]

    return integer
