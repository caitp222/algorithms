from pretty_board import pretty_board, pretty_matrix
from solved_checker import is_solved
from solution_helpers import create_matrix, create_box_possibilities, populate_possibilities, flatten_matrix

def sudoku_solve(st):
    sudoku_matrix = create_matrix(st)
    while is_solved(sudoku_matrix) == False:
        populate_possibilities(sudoku_matrix)
        flatten_matrix(sudoku_matrix)
        pretty_matrix(sudoku_matrix)
        print "\n"
    return sudoku_matrix

# runner/debugging code

puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
puzzle = "--5-3--819-285--6-6----4-5---74-283-34976---5--83--49-15--87--2-9----6---26-495-3"
# puzzle = "316578492529134768487629531263415987974863125851792643138947256692351874745286319"
# pretty_board(puzzle)
# print is_solved(create_matrix(puzzle))
ans = sudoku_solve(puzzle)
# print len(ans)
# print len(ans[0])
# for row in ans:
    # print row
# print sudoku_solve(puzzle)
# print create_box_possibilities(create_matrix(puzzle),0,8)
# print create_box_possibilities(create_matrix(puzzle),6,0)
# print create_box_possibilities(create_matrix(puzzle),6,6)
