from pretty_board import pretty_board
from solved_checker import is_solved
from create_matrix import create_matrix

possibilities = ["1","2","3","4","5","6","7","8","9"]

def sudoku_solve(st):
    sudoku_matrix = create_matrix(st)
    for i in range(len(sudoku_matrix)):
        for j in range(len(sudoku_matrix[0])):
            if sudoku_matrix[i][j] == "-":
                sudoku_matrix[i][j] = [x for x in possibilities if x not in sudoku_matrix[i]]
                for k in range(len(sudoku_matrix)):
                    if type(sudoku_matrix[k][j]) is not list and sudoku_matrix[k][j] in sudoku_matrix[i][j]:
                        sudoku_matrix[i][j].remove(sudoku_matrix[k][j])
    return sudoku_matrix

def create_box(st, x, y):
    sudoku_matrix = create_matrix(st)
    if x <= 2:
        if y <= 2:
            pass
        elif y >= 3 and y <= 5:
            pass
        elif y >= 6:
            pass
    elif x >= 3 and x <= 5:
        if y <= 2:
            pass
        elif y >= 3 and y <= 5:
            pass
        elif y >= 6:
            pass
    elif x >= 6:
        if y <= 2:
            pass
        elif y >= 3 and y <= 5:
            pass
        elif y >= 6:
            pass
    return sudoku_matrix




puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle = "316578492529134768487629531263415987974863125851792643138947256692351874745286319"
# pretty_board(puzzle)
# print is_solved(puzzle)
ans = sudoku_solve(puzzle)
# for row in ans:
    # print row
# print sudoku_solve(puzzle)
print create_box(puzzle,0,0)
