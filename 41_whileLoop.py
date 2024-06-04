# Syntax -->
'''
initialization
while (condition):
    //code
    increment/dicrement
'''
i = 1
while (i <= 10):
    print(i)
    i += 1

'''
print this, using while loop
*
* *
* * *
* * * *
* * * * *
'''
i = 1
while (i<=5):
    j = 1
    while (j <= i):
        print("*", end='')
        j += 1
    print("\n")
    i+=1

# short cut:-
i =1
while(i <=5):
    print(i * "* ")
    i += 1
