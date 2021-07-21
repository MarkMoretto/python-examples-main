
'''
Summary: ASCII to binary with zero-padded output

Date: 2021-05-02

Contributor:
    mark moretto

Requirements:
    Python 3.6+
    
From command line, all are equivalent:
    >>> python ascii_to_bin.py
    >>> python ascii_to_bin.py Hello, World!
    >>> python ascii_to_bin.py "Hello, World!"
    >>> python ascii_to_bin.py 'Hello, World!'
    
The script defaults to the value Hello, World! if no argument passed.
The script stripts single- and double-quotation marks before processing.
'''

import re
from sys import version_info as vi, argv

"""Version check."""
if int(f"{vi.major}{vi.minor}") < 36:
    raise ValueError("Program requires Python v. 3.6 or better.")


"""Default phrase to convert if no argument passed."""
DEFAULT_PHRASE: str = "Hello, World!"


def dec_to_bin(decimal_number: int) -> str:
    """Convert decimal number to binary.
    
    Examples:
    >>> dec_to_bin(5)
    '101'
    >>> dec_to_bin("Q")
    Traceback (most recent call last):
        ...
    ValueError: Integer value expected!   
    """
    
    # Check for correct argument type.
    if not isinstance(decimal_number, int):
        raise ValueError("Integer value expected!")

    # Empty string for outputting results.
    out: str = ""

    # Worker variable to process decmal_number.
    n: int = decimal_number

    # Append remainder of decimal number divided by 2 to `out`
    # Set `n` to quotient of the prior decimal number divided by 2.
    while n > 0:
        out += f"{n % 2}"
        n //= 2
    
    # Reverse binary result before returning the value.
    return out[::-1]



"""Lambda function to convert ASCII character to binary, zero-padded output
using standard, built-in functions.
"""
bin_num = lambda character, z_pad = 8: f'{bin(ord(character)).split("b")[1]:0>{z_pad}}'


"""Lambda function to convert ASCII character to binary, zero-padded output
using the dec_to_bin() function in this script.
"""
bin_num_2 = lambda character, z_pad = 8: f'{dec_to_bin(ord(character)):0>{z_pad}}'



if __name__ == "__main__":
    import doctest
    opt_flags = doctest.IGNORE_EXCEPTION_DETAIL|doctest.FAIL_FAST
    
    n_failed, total_tests = doctest.testmod(optionflags=opt_flags)
    if n_failed > 0:
        print(f"{n_failed} failures out of {total_tests} tests")
        exit(2)

    # Command line input handling.
    try:
        PHRASE_TO_CONVERT = argv[1]
        if not isinstance(PHRASE_TO_CONVERT, str):
            raise ValueError("Please pass character or phrase to convert.")

        # Remove single and double quotation marks before processing.
        PHRASE_TO_CONVERT = re.sub(r"[\"']+", "", PHRASE_TO_CONVERT)
    except IndexError:
        PHRASE_TO_CONVERT = DEFAULT_PHRASE

    # Map and join binary results without spacing for output.
    result = "".join(map(lambda w: bin_num(w), list(PHRASE_TO_CONVERT)))
    
    print(result)
