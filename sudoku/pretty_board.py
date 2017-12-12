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
