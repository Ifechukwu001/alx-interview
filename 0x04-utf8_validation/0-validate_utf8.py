#!/usr/bin/python3
"""A method that determines if a given data set
   represents a valid UTF-8 encoding.

"""
HEAD2_BYTE = "110"
HEAD3_BYTE = "1110"
HEAD4_BYTE = "11110"
CONT_BYTE = "10"


def check_char(code_list, current, result, no_2_check):
    """Checks if the characters following the header are valid.

    Args:
        code_list (list[int]): Data.
        current (int): Index currently checking.
        result (bool): Final result.
        no_2_check (int): Number of bytes to check next.
    """
    if no_2_check:
        if current >= len(code_list):
            return False
        rep = bin(code_list[current]).split("b")[1]
        if len(rep) != 8 or rep[:2] != CONT_BYTE:
            result = False
        return check_char(code_list, current + 1, result, no_2_check - 1)
    else:
        return result


def validUTF8(data):
    """Validates a data set of bytes represented as integers.

    Args:
        data (list[int]): Data set.

    Returns:
        bool: True if the whole set is valid UTF-8, False otherwise
    """
    byte = 0
    result = True

    if type(data) != list and byte == len(data):
        return False
    while byte < len(data):
        rep = bin(data[byte]).split("b")[1]
        if len(rep) <= 7:
            byte += 1
        elif len(rep) == 8:
            if rep[:3] == HEAD2_BYTE:
                result = check_char(data, byte + 1, result, 1)
                byte += 2
            elif rep[:4] == HEAD3_BYTE:
                result = check_char(data, byte + 1, result, 2)
                byte += 3
            elif rep[:5] == HEAD4_BYTE:
                result = check_char(data, byte + 1, result, 3)
                byte += 4
            else:
                result = False
        else:
            result = False
        if not result:
            break
    return result
