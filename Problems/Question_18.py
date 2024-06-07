# Python program to check Armstrong Number.
num = int(input("Enter a number: "))
t = num
n = 0
sum = 0
while(t != 0):
    n = t % 10
    sum += (n ** 3)
    t = t // 10
if(sum == num):
    print("Armstrong")
else:
    print("Not a Armstrong")