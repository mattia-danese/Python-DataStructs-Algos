"""
Problem statement: Given an input string, determine if it makes a valid number 
or not. For simplicity, assume that white spaces are not present in the input.

"""

from unicodedata import decimal


def isValidNum(s):
    s = s.split(".")

    if len(s) > 2: # at most one decimal point
        return False

    for c in "".join(s):
        if ord(c) < 48 or ord(c) > 57: # checks for only digits
            return False
    
    return True


if __name__ == "__main__":
    s = "12234"
    assert(isValidNum(s))
    s = "12234.352"
    assert(isValidNum(s))
    s = "12234.34534.353"
    assert(not isValidNum(s))
    s = "122fg0n34093gegiong34"
    assert(not isValidNum(s))

