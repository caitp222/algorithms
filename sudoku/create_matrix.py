def create_matrix(st):
    sudoku_matrix = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(st[i * 9 + j])
        sudoku_matrix.append(row)
    return sudoku_matrix
