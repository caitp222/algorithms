# turn string into a matrix
def create_matrix(st):
    sudoku_matrix = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(st[i * 9 + j])
        sudoku_matrix.append(row)
    return sudoku_matrix

# create an array with the numbers (no "-"s) that are in the cell's box
# def create_box(st, x, y):
#     box = []
#     x_factor = x/3
#     y_factor = y/3
#     for x in range(3 * x_factor, 3 * (x_factor + 1)):
#         for y in range(3 * y_factor, 3 * (y_factor + 1)):
#             if st[9 * x + y] != "-":
#                 box.append(st[9 * x + y])
#     return box

def create_box(arr, x, y):
    box = []
    x_factor = x/3
    y_factor = y/3
    for x in range(3 * x_factor, 3 * (x_factor + 1)):
        for y in range(3 * y_factor, 3 * (y_factor + 1)):
            if arr[x][y] != "-":
                box.append(arr[x][y])
    return box
