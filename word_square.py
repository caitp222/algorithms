def is_word_square(lst, x = 0, y = 0):
    if len(lst) == 0 or len(lst) != len(lst[0]):
        return False
    elif lst[x][y] != lst[y][x]:
        return False
    else:
        if is_valid_path(lst, x + 1, y):
            return is_word_square(lst, x + 1, y)
        elif is_valid_path(lst, x, y + 1):
            return is_word_square(lst, x, y + 1)
    return True

def is_valid_path(lst, x, y):
    return x < len(lst) and y < len(lst[0])

def create_word_squares(lst, partial = [], ans = []):
    if is_word_square(partial):
        ans.append(partial)
    elif len(partial) > len(lst[0]):
        return
    for i in range(len(lst)):
        remaining = lst[:i] + lst[i + 1:]
        create_word_squares(remaining, partial + [lst[i]], ans)
    return ans

print(create_word_squares(["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]))
