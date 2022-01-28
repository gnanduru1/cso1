import random
import math
from termcolor import colored

data = open(input(''), 'r').read()
g = 5
r = 0
for i in range(g):
    ind = random.randint(50, len(data))
    print(colored(data[ind-50:ind], 'white', 'on_green'))
    guess = input("What is your guess?\n")
    if guess == data[ind+1]: r += 1


print("You got {} out of {} guesses correct!".format(r, g))
print(math.log(g/r, 2))