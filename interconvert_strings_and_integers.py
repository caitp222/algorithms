# A string is a sequence of characters. A string may encode an integer, e.g., "-987" encodes -987.
# Implement methods that take a string representing an integer and return the corresponding integer, and vice versa.
# Your code should handle negative integers. You cannot use library fucntions like stoi in C++ and parseInt in Java.

import math

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

def int_to_string(n):
    conversion_dict = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
    }
    if n < 0:
        x = n * -1
    else:
        x = n
    length = int(math.log10(x)) + 1
    number = []
    for i in range(length):
        second = (x%10**(i+1))/10**i
        number.insert(0, conversion_dict[second])
    if x != n:
        number.insert(0, '-')
    number = ''.join(x for x in number)
    return number


print(string_to_int("-8592457567"))
print(int_to_string(-8592457567))
