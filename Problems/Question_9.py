# Python program to check Leap year
y = int(input("Enter a year: "))
if (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0):
    print("This is a Leap Year")
else:
    print("Not a Leap Year")