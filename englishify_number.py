def englishify(num):
    englishified_string = ""
    decoder = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    digits = num % 10
    tens = num % 100 - digits
    if tens == 10:
        teens = num % 100
    else:
        teens = False
    hundreds = num % 1000 / 100
    thousands = num % 10000 / 1000
    ten_thousands = num % 100000 / 10000 * 10
    if ten_thousands == 10:
        teen_thousands = num % 100000 / 1000
    else:
        teen_thousands = False
    hundred_thousands = num % 1000000 / 100000
    millions = num % 10000000 / 1000000
    if millions is not 0:
        englishified_string += decoder[millions] + " million "
    if hundred_thousands is not 0:
        englishified_string += decoder[hundred_thousands] + " hundred "
    if num > 100000:
        englishified_string += "and "
    if num > 10000 and teen_thousands:
        englishified_string += decoder[teen_thousands] + " thousand "
    elif num > 10000:
        englishified_string += decoder[ten_thousands] + " "
        if thousands is not 0:
            englishified_string += decoder[thousands] + " thousand "
    if hundreds is not 0:
        englishified_string += decoder[hundreds] + " hundred "
    if num > 100 and tens is not 0 and digits is not 0:
        englishified_string += "and "
    if teens:
        englishified_string += decoder[teens]
    else:
        englishified_string += decoder[tens] + " "
        englishified_string += decoder[digits]
    return englishified_string

print englishify(1567034)
print englishify(8900)
print englishify(16917)
