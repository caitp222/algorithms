from pretty_board import pretty_board, pretty_matrix
from solved_checker import is_solved
from solution_helpers import create_matrix, create_box_possibilities, populate_possibilities, flatten_matrix

def sudoku_solve(puzzle):
    if type(puzzle) == str:
        puzzle = create_matrix(puzzle)
    # base case
    if is_solved(puzzle):
        return puzzle
    else:
        pretty_matrix(puzzle)
        populate_possibilities(puzzle)
        solutions_count = flatten_matrix(puzzle)
        if solutions_count > 0:
            return sudoku_solve(puzzle)
        else:
            guess = False
            for i in range(len(puzzle)):
                for j in range(len(puzzle[0])):
                    if len(puzzle[i][j]) > 1:
                        puzzle[i][j] = puzzle[i][j][0]
                        guess = True
                        break
                if guess:
                    break
            return sudoku_solve(puzzle)
        return False


puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# pretty_matrix(sudoku_solve(puzzle))
# print
sudoku_solve(puzzle)
