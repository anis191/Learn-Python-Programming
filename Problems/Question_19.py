# Python program to find Armstrong Number in an interval.
a = int(input("From: "))
b = int(input("To: "))
for num in range(a, b+1):
    order = len(str(num))
    temp = num
    r = 0
    sum = 0
    while(temp != 0):
        r = temp % 10
        sum += (r ** order)
        temp = temp // 10
    if(sum == num):
        print(num)
    else:
        continue