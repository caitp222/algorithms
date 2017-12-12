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
    pass

puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
pretty_board(puzzle)
