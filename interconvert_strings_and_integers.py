# A string is a sequence of characters. A string may encode an integer, e.g., "-987" encodes -987.
# Implement methods that take a string representing an integer and return the corresponding integer, and vice versa.
# Your code should handle negative integers. You cannot use library fucntions like stoi in C++ and parseInt in Java.

def string_to_int(str):
    conversion_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    res = 0
    index = 0
    for char in str[::-1]:
        if char == "-":
            res *= -1
        else:
            res += conversion_dict[char] * 10**index
            index += 1
    return res

print(string_to_int("-8592457567"))
