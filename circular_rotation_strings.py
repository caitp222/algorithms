# Check if a given string can be derived from another string by circularly rotating it.
# The rotation can be clockwise or anti-clockwise in direction.

# solution 1
def circular_rotation1(str1, str2):
    str11 = str1 + str1
    if str2 in str11:
        return True
    else:
        return False

# solution 2
def circular_rotation2(str1, str2):
    for i in range(0, len(str1)):
        str1 = str1[1:] + str1[0]
        if str1 == str2:
            return True
        else:
            i += 1
    return False

print(circular_rotation1("ABCD", "DABC"))
print(circular_rotation2("ABCD", "DABC"))
