from pretty_board import pretty_board, pretty_matrix
from solved_checker import is_solved
from solution_helpers import create_matrix, create_box_possibilities, populate_possibilities, flatten_matrix

import copy

def sudoku_solve(puzzle):
    if type(puzzle) == str:
        puzzle = create_matrix(puzzle)
    populate_possibilities(puzzle)
    while flatten_matrix(puzzle) > 0:
        populate_possibilities(puzzle)
    if is_solved(puzzle):
        pretty_matrix(puzzle)
        return True
    new_puzzle = copy.deepcopy(puzzle)
    for i in range(len(new_puzzle)):
        for j in range(len(new_puzzle[0])):
            if len(new_puzzle[i][j]) > 1:
                possibles = new_puzzle[i][j]
                for possibility in possibles:
                    new_puzzle[i][j] = possibility
                    if sudoku_solve(new_puzzle) == True:
                        return True
    return False

puzzle = "-3-5--8-45-42---1---8--9---79-8-61-3-----54---5------78-----7-2---7-46--61-3--5--"
print sudoku_solve(puzzle)
