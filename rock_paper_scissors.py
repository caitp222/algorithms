# Write a program that can take in two responses for a rock-paper-scissors game and declare who the winner is.

def rock_paper_scissors(move1, move2):
    loses_to = {
        "paper" : "scissors",
        "scissors" : "rock",
        "rock" : "paper"
    }
    if move1 == move2:
        return "no winner"
    elif move2 == loses_to[move1]:
        return "%s is the winner" %(move2)
    else:
        return "%s is the winner" %(move1)


print rock_paper_scissors("paper", "paper")
print rock_paper_scissors("paper", "rock")
print rock_paper_scissors("paper", "scissors")
