# Divide two numbers without using "/" operator

# interative
def iterative_division(num1, num2):
    if num1 < num2:
        return "Quotient is 0, remainder is %i" %(num1)
    else:
        quotient = 0
        while num1 >= num2:
            num1 -= num2
            quotient += 1
        return "Quotient is %i, remainder is %i" %(quotient, num1)

# recursive
def recursive_division(num1, num2):
    if num1 < num2:
        return 0
    elif num2 + num2 - num1 <= num2:
        return recursive_division(num1 - num2, num2) + 1



print(iterative_division(10, 5))
print(iterative_division(145, 12))
print(iterative_division(5,6))
print(recursive_division(10, 5))
print(recursive_division(145, 12))
print(recursive_division(5,6))
