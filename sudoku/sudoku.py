def pretty_board(st):
    board = ""
    for x in range(len(st)):
        board += st[x]
        if (x + 1) % 27 == 0:
            board += "\n\n"
        elif (x + 1) % 9 == 0:
            board += "\n"
        elif (x + 1) % 3 == 0:
            board += "   "
    print board

def is_solved(st):
    sorted_arr = ["1","2","3","4","5","6","7","8","9"]
    matrix_rows = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(st[i * 9 + j])
        matrix_rows.append(row)
    matrix_columns = []
    for i in range(9):
        column = []
        for j in range(9):
            column.append(matrix_rows[j][i])
        matrix_columns.append(column)
    matrix_boxes = []
    for h in range(3):
        for i in range(3):
            box = []
            for j in range(3):
                for k in range(3):
                    box.append(matrix_rows[3 * i + j][3 * h + k])
            matrix_boxes.append(box)
    for matrix in matrix_columns:
        if matrix.sort() != sorted_arr:
            return False
    for matrix in matrix_rows:
        if matrix.sort() != sorted_arr:
            return False
    for matrix in matrix_boxes:
        if matrix.sort() != sorted_arr:
            return False
    return True


puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle = "316578492529134768487629531263415987974863125851792643138947256692351874745286319"
pretty_board(puzzle)
print is_solved(puzzle)
