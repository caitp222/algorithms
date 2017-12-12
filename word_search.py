# iterative
# problems with order of if statements
# def word_search(arr, word, top=0, left=0):
#     while True:
#         if arr[top][left] == word[0]:
#             i = top
#             j = left
#             x = 1
#             found = True
#             while found == True:
#                 while x < len(word):
#                     if is_valid_path(arr, i, j + 1) and arr[i][j + 1] == word[x]:
#                         j += 1
#                     elif is_valid_path(arr, i - 1, j + 1) and arr[i - 1][j + 1] == word[x]:
#                         j += 1
#                         i -= 1
#                     elif is_valid_path(arr, i + 1, j) and arr[i + 1][j] == word[x]:
#                         i += 1
#                     elif is_valid_path(arr, i - 1, j) and arr[i - 1][j] == word[x]:
#                         i -= 1
#                     elif is_valid_path(arr, i, j - 1) and arr[i][j - 1] == word[x]:
#                         j -= 1
#                     elif is_valid_path(arr, i + 1, j + 1) and arr[i + 1][j + 1] == word[x]:
#                         j += 1
#                         i += 1
#                     elif is_valid_path(arr, i - 1, j - 1) and arr[i - 1][j - 1] == word[x]:
#                         j -= 1
#                         i -= 1
#                     elif is_valid_path(arr, i + 1, j - 1) and arr[i + 1][j - 1] == word[x]:
#                         j -= 1
#                         i += 1
#                     else:
#                         found = False
#                         break
#                     if x == len(word) - 1 and found == True:
#                         return True
#                     x += 1
#         left += 1
#         if left == len(arr[0]) - 1 and top == len(arr) - 1:
#             return False
#         elif left == len(arr[0]) - 1:
#             left = 0
#             if top < len(arr) - 1:
#                 top += 1

# recursive
def word_search(arr, word, i=0, j=0, x=0, letters_found = []):
    if x == len(word) - 1 and len(word) - 1 == len(letters_found) and arr[i][j] == word[x]:
        return True
    elif i == len(arr) - 1 and j == len(arr[0]) - 1:
        return False
    elif arr[i][j] == word[x] and x < len(word) - 1:
        letters_found.append(word[x])
        x += 1
        if is_valid_path(arr, i, j + 1) and arr[i][j + 1] == word[x]:
            j += 1
        elif is_valid_path(arr, i - 1, j + 1) and arr[i - 1][j + 1] == word[x]:
            j += 1
            i -= 1
        elif is_valid_path(arr, i + 1, j) and arr[i + 1][j] == word[x]:
            i += 1
        elif is_valid_path(arr, i - 1, j) and arr[i - 1][j] == word[x]:
            i -= 1
        elif is_valid_path(arr, i, j - 1) and arr[i][j - 1] == word[x]:
            j -= 1
        elif is_valid_path(arr, i + 1, j + 1) and arr[i + 1][j + 1] == word[x]:
            j += 1
            i += 1
        elif is_valid_path(arr, i - 1, j - 1) and arr[i - 1][j - 1] == word[x]:
            j -= 1
            i -= 1
        elif is_valid_path(arr, i + 1, j - 1) and arr[i + 1][j - 1] == word[x]:
            j -= 1
            i += 1
        return word_search(arr, word, i, j, x, letters_found)
    elif j < len(arr[0]) - 1:
        j += 1
        return word_search(arr, word, i, j, x, letters_found)
    elif j == len(arr[0]) - 1 and i < len(arr) - 1:
        j = 0
        i += 1
        return word_search(arr, word, i, j, x, letters_found)


def is_valid_path(arr, i, j):
    return i >= 0 and i < len(arr[0]) and j >= 0 and j < len(arr)


puzzle = [
  ["a", "w", "o", "l", "v", "e", "s"],
  ["s", "o", "a", "w", "a", "h", "p"],
  ["i", "t", "c", "k", "e", "t", "n"],
  ["o", "t", "s", "d", "h", "o", "h"],
  ["s", "e", "h", "g", "s", "t", "a"],
  ["u", "r", "p", "i", "w", "e", "u"],
  ["z", "s", "b", "n", "u", "i", "r"]
]

word = "wolves"
print word_search(puzzle, word, 0, 0, 0, [])
word = "otters"
print word_search(puzzle, word, 0, 0, 0, [])
word = "bison"
print word_search(puzzle, word, 0, 0, 0, [])
word = "nighthawks"
print word_search(puzzle, word, 0, 0, 0, [])
word = "unitedkingdom"
print word_search(puzzle, word, 0, 0, 0, [])
