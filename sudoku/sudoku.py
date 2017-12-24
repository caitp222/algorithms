from pretty_board import pretty_board, pretty_matrix
from solved_checker import is_solved
from solution_helpers import create_matrix, create_box_possibilities, populate_possibilities, flatten_matrix

import copy

def sudoku_solve(puzzle):
    if type(puzzle) == str:
        puzzle = create_matrix(puzzle)
    populate_possibilities(puzzle)
    # pretty_matrix(puzzle)
    while flatten_matrix(puzzle) > 0:
        populate_possibilities(puzzle)
    if is_solved(puzzle):
        print "solved!!"
        pretty_matrix(puzzle)
        return True
    new_puzzle = copy.deepcopy(puzzle)
    for i in range(len(new_puzzle)):
        for j in range(len(new_puzzle[0])):
            if len(new_puzzle[i][j]) > 1:
                possibles = new_puzzle[i][j]
                for possibility in possibles:
                    new_puzzle[i][j] = possibility
                    # print "blooooooop"
                    # pretty_matrix(new_puzzle)
                    if sudoku_solve(new_puzzle) == True:
                        return True
                    else:
                        continue
            elif len(new_puzzle[i][j]) < 1:
                new_puzzle = copy.deepcopy(puzzle)
                continue
    return False

puzzle = "-3-5--8-45-42---1---8--9---79-8-61-3-----54---5------78-----7-2---7-46--61-3--5--"
print sudoku_solve(puzzle)

puzzle = "-96-4---11---6---45-481-39---795--43-3--8----4-5-23-18-1-63--59-59-7-83---359---7"
print sudoku_solve(puzzle)
