from pretty_board import pretty_board, pretty_matrix
from solved_checker import is_solved
from solution_helpers import create_matrix, create_box_possibilities, populate_possibilities, flatten_matrix

def sudoku_solve(puzzle):
    if type(puzzle) == str:
        puzzle = create_matrix(puzzle)
    pretty_matrix(puzzle)
    populate_possibilities(puzzle)
    while flatten_matrix(puzzle) > 0:
        print "\n"
        flatten_matrix(puzzle)
        populate_possibilities(puzzle)
        pretty_matrix(populate_possibilities(puzzle))
    assigned = False
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if len(puzzle[i][j]) > 1:
                # print puzzle[i][j]
                possibles = puzzle[i][j]
                assigned = True
                break
        if assigned:
            break
    puzzle[i][j] = [possibles[1]]
    pretty_matrix(puzzle)
    while flatten_matrix(puzzle) > 0:
        print "\n"
        flatten_matrix(puzzle)
        populate_possibilities(puzzle)
        pretty_matrix(populate_possibilities(puzzle))
    assigned = False
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if len(puzzle[i][j]) > 1:
                # print puzzle[i][j]
                possibles = puzzle[i][j]
                assigned = True
                break
        if assigned:
            break
    puzzle[i][j] = [possibles[0]]
    pretty_matrix(puzzle)
    while flatten_matrix(puzzle) > 0:
        print "\n"
        flatten_matrix(puzzle)
        populate_possibilities(puzzle)
        pretty_matrix(populate_possibilities(puzzle))
    print is_solved(puzzle)



puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle = "--5-3--819-285--6-6----4-5---74-283-34976---5--83--49-15--87--2-9----6---26-495-3"
# puzzle = "29-5----77-----4----4738-129-2--3-648---5--7-5---672--3-9--4--5----8-7---87--51-9"
# puzzle = "-8--2-----4-5--32--2-3-9-466---9---4---64-5-1134-5-7--36---4--24-723-6-----7--45-"
# puzzle = "6-873----2-----46-----6482--8---57-19--618--4-31----8-86-2---39-5----1--1--4562--"
# pretty_matrix(sudoku_solve(puzzle))
sudoku_solve(puzzle)
# print sudoku_solve(puzzle)
