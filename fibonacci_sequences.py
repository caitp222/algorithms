# top down memoization
# def fib_top(n):
#     fib_dict = {}
#     if n == 1:
#         fib_dict[n] = n
#         return n
#     else:
#         return fib_dict[n - 2] + fib(n - 1)



# bottom up memoization
def fib_bottom(n):
    fib_dict = {0: 0, 1: 1}
    if n is not 0:
        for x in range(2, n + 1):
            fib_dict[x] = fib_dict[x - 1] + fib_dict[x - 2]
            print(fib_dict)
    return fib_dict[n]

# print(fib_top(17) == 1597)
print(fib_bottom(17) == 1597)
