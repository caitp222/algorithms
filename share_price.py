# Imagine after your first pay check from your first job as an amazing lady programmer,
# you invested a portion of it into some stock market shares.
# Now imagine that a few years later you want to see how much those shares are worth
# but for some bizarre reason you wanted to figure it out yourself with a list of days
# and the percentage change of the value of those share. How could you go about it?

def share_price(initial_investment, lst):
    res = initial_investment
    for day, percentage in lst:
        res *= (1 + percentage)
    return res

initial_investment = 100
lst = [["Monday", -0.2], ["Tuesday", 0.7], ["Wednesday", 0.02], ["Thursday", 0.19], ["Friday", - 0.01]]
print share_price(initial_investment, lst)
