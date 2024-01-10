#!/usr/bin/python3
def subtract_from_list(list_num):
    subtract_total = 0
    max_value = max(list_num)

    for num in list_num:
        if max_value > num:
            subtract_total += num

    return (max_value - subtract_total)


def roman_to_integer(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_keys = list(roman_numerals.keys())

    num = 0
    last_numeral = 0
    numeral_list = [0]

    for character in roman_string:
        for numeral in numeral_keys:
            if numeral == character:
                if roman_numerals.get(character) <= last_numeral:
                    num += subtract_from_list(numeral_list)
                    numeral_list = [roman_numerals.get(character)]
                else:
                    numeral_list.append(roman_numerals.get(character))

                last_numeral = roman_numerals.get(character)

    num += subtract_from_list(numeral_list)

    return num
