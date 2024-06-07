# Python program to check prime numbers.
num = int(input("Enter a number: "))
if(num > 1):
    count = 0
    for i in range(2, num):
        if(num % i == 0):
            count += 1
            break
        else:
            continue
    if(count == 0):
        print("It's a Prime")
    else:
        print("Not a Prime")
else:
    print("Not a Prime")