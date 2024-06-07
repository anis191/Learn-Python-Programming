# Python program to print all prime numbers in a interval
s = int(input("From: "))
e = int(input("To: "))

for num in range(s, e+1):
    if(num > 1):
        count = 0
        for i in range(2, num):
            if(num % i == 0):
                count +=1
                break
            else:
                continue
        if(count == 0):
            print(num, end=' ')
        else:
            continue
    else:
        continue