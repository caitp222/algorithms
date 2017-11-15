# top down memoization

fib_dict = {0: 0, 1: 1}
def fib_1(n):
    if n <= 1:
        return n
    elif n not in fib_dict:
        fib_dict[n] = fib_1(n - 1) + fib_dict[n - 2]
    return fib_dict[n]

# bottom up memoization
def fib_2(n):
    fib_dict = {0: 0, 1: 1}
    if n is not 0 or 1:
        for x in range(2, n + 1):
            fib_dict[x] = fib_dict[x - 1] + fib_dict[x - 2]
    return fib_dict[n]

print(fib_1(17) == 1597)
print(fib_2(17) == 1597)
