cell_possibilities = ["1","2","3","4","5","6","7","8","9"]

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
def create_box_possibilities(arr, x, y):
    box = []
    x_factor = x/3
    y_factor = y/3
    for x in range(3 * x_factor, 3 * (x_factor + 1)):
        for y in range(3 * y_factor, 3 * (y_factor + 1)):
            if arr[x][y] != "-":
                box.append(arr[x][y])
    return box

# replace "-" with arrays of possibilities, or recalculates the possiblities in the array
def populate_possibilities(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "-" or type(arr[i][j]) is list:
                if arr[i][j] == "-":
                    arr[i][j] = [x for x in cell_possibilities if x not in arr[i]]
                for k in range(len(arr)):
                    if type(arr[k][j]) is not list and arr[k][j] in arr[i][j]:
                        arr[i][j].remove(arr[k][j])
                box = create_box_possibilities(arr, i, j)
                for el in box:
                    if el in arr[i][j]:
                        arr[i][j].remove(el)
    return arr

# if an element is an array of length 1, it flattens it
def flatten_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if type(arr[i][j]) is list and len(arr[i][j]) == 1:
                arr[i][j] = arr[i][j][0]
    return arr
