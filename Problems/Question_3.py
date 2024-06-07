# Python program to find the square root.
'''
Square Root:
√49 --> 49^(1/2)
'''
num = int(input("Enter a number: "))
sq = num ** (1/2)
print("The square root of the given number is: ", sq)

# We also solve this using "sqrt()" function. Which function library is --> "math"
'''
import math
num = int(input("Enter a number: "))
sq = math.sqrt(num)
print("The square root of the given number is: ", sq)
'''