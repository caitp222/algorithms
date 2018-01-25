def is_word_square(lst, x = 0, y = 0):
    if lst[x][y] != lst[y][x]:
        return False
    else:
        if is_valid_path(lst, x + 1, y):
            return is_word_square(lst, x + 1, y)
        elif is_valid_path(lst, x, y + 1):
            return is_word_square(lst, x, y + 1)
    return True

def is_valid_path(lst, x, y):
    return x < len(lst) and y < len(lst[0])



print(is_word_square(["BALL", "AREA", "LEAD", "LADY"]))
