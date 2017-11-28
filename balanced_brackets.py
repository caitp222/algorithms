def balanced_brackets(str):
    matches = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    arr = []
    for i in range(0, len(str)):
        if str[i] in matches.keys():
            arr.append(str[i])
        elif str[i] in matches.values() and len(arr) == 0:
            return False
        elif str[i] in matches.values() and matches[arr[-1]] == str[i]:
            arr = arr[:-1]
        else:
            return False
    return len(arr) == 0



print(balanced_brackets("{[()]}"))
print(balanced_brackets("{[(])}"))
print(balanced_brackets("{{[[(())]]}}"))
print(balanced_brackets("((((((((()))))"))
