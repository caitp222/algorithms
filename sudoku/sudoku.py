from pretty_board import pretty_board
from solved_checker import is_solved

def sudoku_solve(st):
    pass


puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle = "316578492529134768487629531263415987974863125851792643138947256692351874745286319"
pretty_board(puzzle)
print is_solved(puzzle)
