from pretty_board import pretty_board, pretty_matrix
from solved_checker import is_solved
from solution_helpers import create_matrix, create_box_possibilities, populate_possibilities, flatten_matrix

import copy

def sudoku_solve(puzzle):
    if type(puzzle) == str:
        puzzle = create_matrix(puzzle)
    else:
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                if len(puzzle[i][j]) < 1:
                    return False
    populate_possibilities(puzzle)
    # pretty_matrix(puzzle)
    while flatten_matrix(puzzle) > 0:
        populate_possibilities(puzzle)
    if is_solved(puzzle):
        # pretty_matrix(puzzle)
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

def run_all_sudoku():
    path = '/users/Caitlin/practice/algorithms/sudoku/sudoku_puzzles.txt'
    puzzles_file = open(path, 'r')
    for line in puzzles_file.readlines():
        print sudoku_solve(line[:-1])

run_all_sudoku()


# puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle = "--5-3--819-285--6-6----4-5---74-283-34976---5--83--49-15--87--2-9----6---26-495-3"
# puzzle = "29-5----77-----4----4738-129-2--3-648---5--7-5---672--3-9--4--5----8-7---87--51-9"
# puzzle = "-8--2-----4-5--32--2-3-9-466---9---4---64-5-1134-5-7--36---4--24-723-6-----7--45-"
# puzzle = "6-873----2-----46-----6482--8---57-19--618--4-31----8-86-2---39-5----1--1--4562--"
# puzzle = "---6891--8------2915------84-3----5-2----5----9-24-8-1-847--91-5------6--6-41----"
# puzzle = "-3-5--8-45-42---1---8--9---79-8-61-3-----54---5------78-----7-2---7-46--61-3--5--" #False
# puzzle = "-96-4---11---6---45-481-39---795--43-3--8----4-5-23-18-1-63--59-59-7-83---359---7"
# puzzle = "----754----------8-8-19----3----1-6--------34----6817-2-4---6-39------2-53-2-----" #False
# puzzle = "3---------5-7-3--8----28-7-7------43-----------39-41-54--3--8--1---4----968---2--" #False
# puzzle = "3-26-9--55--73----------9-----94----------1-9----57-6---85----6--------3-19-82-4-" #False
# puzzle = "-2-5----48-5--------48-9-2------5-73-9-----6-25-9------3-6-18--------4-71----4-9-"
# puzzle = "--7--8------2---6-65--79----7----3-5-83---67-2-1----8----71--38-2---5------4--2--" #Loooooooong
# puzzle = "----------2-65-------18--4--9----6-4-3---57-------------------73------9----------" #Loooooooong
# puzzle = "---------------------------------------------------------------------------------" #Loooooooong

# print sudoku_solve(puzzle)
