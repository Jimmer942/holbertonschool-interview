#!/usr/bin/python3
"""
Validate UTF8
"""


def validUTF8(data):
    """ checks data and returns true if data is a valid UTF-8 encoding
    """

    number = 0
    higer = 1 << 7
    lower = 1 << 6

    for num in data:
        mask = 1 << 7
        if number == 0:
            while mask & num:
                number += 1
                mask = mask >> 1

            if number == 0:
                continue

            if number == 1 or number > 4:
                return False
        else:
            if not (num & higer and not (num & lower)):
                return False
        number -= 1
    is_valid = number == 0
    return is_valid
