# Write a program that uses the Sieve of Eratosthenes to find the sum of all the primes from 2 up to a given number

def sieve(n):
    lst = list(range(2, n + 1))
    for i in range(n):
        if i >= len(lst):
            return sum(lst)
        else:
            for j in range(i + 1, n):
                if j >= len(lst):
                    continue
                elif lst[j] % lst[i] == 0:
                    lst.remove(lst[j])
    return sum(lst)

print(sieve(100) == 1060)
print(sieve(1000) == 76127)
