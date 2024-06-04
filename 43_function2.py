def calculator(a,b,s):
    ans1 = a+b
    ans2 = a-b
    ans3 = a*b
    ans4 = a/b
    ans5 = a%b
    if s == '+':
        return ans1
    elif s == '-':
        return ans2
    elif s == '*':
        return ans3
    elif s == '/':
        return ans4
    elif s == '%':
        return ans5
    else:
        return False

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
s = input("Enter operation(+/-/*/div(/)/%):")
ans = calculator(a,b,s)
if ans == False:
    print("Invalid operation sign!")
else:
    print(ans)