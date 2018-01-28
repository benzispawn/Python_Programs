import random

def makeList():
    numbers = []
    while len(numbers) < 6:
        n = random.randint(1,4)
        numbers.append(n)
    return numbers

def remDuplicates():
    numbers = set(makeList())
    numbers = list(numbers)
    return numbers

print(remDuplicates())
