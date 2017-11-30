# Given a string and a non-empty substring, compute recursively the number of times
# that substring appears in the string, without the sub strings overlapping.
# strCount("catcowcat", "cat") == 2
# strCount("catcowcat", "cow") == 1
# strCount("catcowcat", "dog") == 0

def string_count(str, sub_str):
    if len(str) < len(sub_str):
        return 0
    elif str[:len(sub_str)] == sub_str:
        return 1 + string_count(str[len(sub_str):], sub_str)
    else:
        return string_count(str[1:], sub_str)

print string_count("catcowcat", "cat")
print string_count("catcowcat", "cow")
print string_count("catcowcat", "dog")
