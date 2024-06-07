# Python program to generate a random number
'''
We need to import a module named-->"random" for generate a random number.
This python "random" module have a "randint" method, which generate a random integer number between a number range.
Syntax -->
import random
num = random.randint(starting_number, ending_number)
'''
import random
num = random.randint(0,10)
print(num)