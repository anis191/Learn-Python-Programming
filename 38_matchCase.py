# Like c/c++ switch case
'''
Syntax -->
match x:
    case 1:
        //code
    case 2:
        //code
    ......
    case n:
        //code
    case _:        #like c/c++ switch case default
        //code
'''
num = int(input("Enter a number(1-3): "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid input")

print("Program End")