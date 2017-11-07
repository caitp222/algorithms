# http://www.techiedelight.com/longest-common-substring-problem/
# dynamic programming

def longest_common_substring(str1, str2):
    longest_common_substring = ""
    for i in range(0, len(str1)):
        j = 0
        longest_string_so_far = ""
        while j < len(str2):
            if (i + j) < len(str1) and str1[i + j] == str2[j]:
                longest_string_so_far = longest_string_so_far + str2[j]
            j += 1
        if len(longest_string_so_far) > len(longest_common_substring):
            longest_common_substring = longest_string_so_far
    return longest_common_substring


print longest_common_substring("ABABC", "BABCA") == "BABC"
print longest_common_substring("BABCABA", "BCAB") == "BCAB"
