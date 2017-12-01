# given a sorted dictionary in an alien language, determine the language's alphabet

def alien_alphabet(lst):
    helper_dict = {}
    alphabet = []
    for word in lst:
        if word[0] not in helper_dict.keys():
            helper_dict[word[0]] = []
        else:
            for key in helper_dict:
                if key == word[0]:
                    continue
                else:
                    helper_dict[key].append(word[0])
    for i in range(len(lst)):
        if lst[i - 1] and lst[i][0] == lst[i - 1][0]:
            for j in range(len(lst[i])):
                if lst[i - 1][j] != lst[i][j]:
                    if lst[i - 1][j] not in helper_dict.keys():
                        helper_dict[lst[i - 1][j]] = [lst[i][j]]
                    else:
                        helper_dict[lst[i - 1][j]].append(lst[i][j])
    while len(helper_dict) > 0:
        for key in helper_dict:
            if helper_dict[key] == []:
                alphabet.insert(0, key)
        helper_dict.pop(alphabet[0], None)
        for key in helper_dict:
            if alphabet[0] in helper_dict[key]:
                helper_dict[key].remove(alphabet[0])
    return alphabet

words = ["baa", "abcd", "abca", "cab", "cad"]
print alien_alphabet(words)
