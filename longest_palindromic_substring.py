# Given a string, find max-length contiguous substring of it that is also a palindrome.
# For example, the longest palindromic substring of bananas is anana.
# For example, the longest palindromic substring of ABDCBCDBDCBBC is BDCBCDB

# dynamic programming
def max_palindromic_substring(str):
    max_substr = ""
    for i in range(0, len(str)):
        for j in range(i, len(str)):
            if is_palindrome(str[i:j]) and len(str[i:j]) > len(max_substr):
                max_substr = str[i:j]
            j += 1
        i += 1
    return max_substr


# helper methods
def is_palindrome(str1):
    return str1 == reverse(str1)

def reverse(str):
    i = len(str) - 1
    new_str = ""
    while i >= 0:
        new_str += str[i]
        i -= 1
    return new_str


print(max_palindromic_substring("bananas"))
# print(max_palindromic_substring("ABDCBCDBDCBBC"))
