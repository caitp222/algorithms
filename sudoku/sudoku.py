from pretty_board import pretty_board
from solved_checker import is_solved
from solution_helpers import create_matrix, create_box

cell_possibilities = ["1","2","3","4","5","6","7","8","9"]

def sudoku_solve(st):
    # sudoku_matrix = create_matrix(st)
    sudoku_matrix = populate_possibilities(st)
    for i in range(len(sudoku_matrix)):
        for j in range(len(sudoku_matrix[0])):
            if type(sudoku_matrix[i][j]) is list and len(sudoku_matrix[i][j]) == 1:
                sudoku_matrix[i][j] = sudoku_matrix[i][j][0]
    print is_solved(sudoku_matrix)
    return sudoku_matrix

def populate_possibilities(st):
    sudoku_matrix = create_matrix(st)
    for i in range(len(sudoku_matrix)):
        for j in range(len(sudoku_matrix[0])):
            if sudoku_matrix[i][j] == "-" or type(sudoku_matrix[i][j]) is list:
                sudoku_matrix[i][j] = [x for x in cell_possibilities if x not in sudoku_matrix[i]]
                for k in range(len(sudoku_matrix)):
                    if type(sudoku_matrix[k][j]) is not list and sudoku_matrix[k][j] in sudoku_matrix[i][j]:
                        sudoku_matrix[i][j].remove(sudoku_matrix[k][j])
                box = create_box(sudoku_matrix, i, j)
                for el in box:
                    if el in sudoku_matrix[i][j]:
                        sudoku_matrix[i][j].remove(el)
    return sudoku_matrix



# runner/debugging code

puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle = "316578492529134768487629531263415987974863125851792643138947256692351874745286319"
# pretty_board(puzzle)
# print is_solved(create_matrix(puzzle))
ans = sudoku_solve(puzzle)
# print len(ans)
# print len(ans[0])
for row in ans:
    print row
# print sudoku_solve(puzzle)
print create_box(create_matrix(puzzle),0,8)
print create_box(create_matrix(puzzle),6,0)
print create_box(create_matrix(puzzle),6,6)
