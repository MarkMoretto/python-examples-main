#!/usr/bin/env python3

"""
Purpose: Convert hex code to unicode.
Date created: 2021-11-02

Contributor(s):
    Mark M.
"""


def to_base_16(string: str, index: int) -> int:
    """Return calculated integer value for a given ascii character.
    """
    return int(string, 16) * pow(16, index)


def proc_code(hexcode_string: str) -> int:
    """Return Unicode value for a given hex character code string.
    """
    total = 0
    for idx, item in enumerate(hexcode_string[::-1]):
        total += to_base_16(item, idx)
    return total


def tokenize(string: str, delimiter: str = ",") -> list:
    """Return list of string items with excess whitespace removed.
    """
    return list(map(str.strip, string.split(delimiter)))


def convert_code(hex_code_string) -> str:
    hex_codes = tokenize(hex_code_string)
    return "".join(map(lambda s: chr(s) if s != 0 else "", map(proc_code, hex_codes)))


def test_convert_code():
    expected = r"%systemroot%\system32\cmd.exe,0"

    # Sample hex code string from Windows registry.
    sample = "25,00,73,00,79,00,73,00,74,00,65,00,6d,00,72,00,6f,00,6f,00,74,00,25,00,5c,00,73,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,63,00,6d,00,64,00,2e,00,65,00,78,00,65,00,2c,00,30,00,00,00"

    # Run main function and print output.
    result = convert_code(sample)

    assert (result == expected), "Error: convert_code() test failed."



if __name__ == "__main__":
    # Run simple test
    test_convert_code()

    # Sample hex code string from Windows registry.
    sample = "25,00,73,00,79,00,73,00,74,00,65,00,6d,00,72,00,6f,00,6f,00,74,00,25,00,5c,00,73,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,63,00,6d,00,64,00,2e,00,65,00,78,00,65,00,2c,00,30,00,00,00"

    # Run main function and print output.
    result = convert_code(sample)

    # Sho
    print(result)







# import re
# from functools import partial

# int_hex = partial(int, base=16)

# hex2_code = """
# 25,00,73,00,79,00,73,00,74,00,65,00,6d,00,72,00,6f,00,6f,00,74,\
#   00,25,00,5c,00,73,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,63,00,\
#   6d,00,64,00,2e,00,65,00,78,00,65,00,2c,00,30,00,00,00
# """.strip()
# clean_str = re.sub(r"[^a-zA-Z0-9,]", "", hex2_code)