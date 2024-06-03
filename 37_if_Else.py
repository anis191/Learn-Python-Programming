age = int(input("Enter your age: "))

if(age <= 7):
    print("Child")
elif(age <= 17):
    print("Boy")
elif(age >= 18 and age <= 60):
    print("Adult")
else:
    print("Old")