# Write a function which returns the sum of following series up to nth term(parameter)
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

def series_sum(n):
    res = 0
    for i in range(n):
        res += 1.0/(3*i + 1)
    return res

print(series_sum(6))
