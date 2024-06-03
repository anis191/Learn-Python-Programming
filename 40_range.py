# range(starting_value,ending_value) --> starting_value to (ending_value - 1)
print(range(0,5))

for i in range(0,5): # 0 to (5-1)
    print(i, end=' ')
print("\n")

for i in range(5): # 0(automatic) to (5-1)
    print(i, end=' ')
print("\n")

for i in range(5,10): # 5 to (10-1)
    print(i, end=' ')
print("\n")

# Print number table:
i = int(input("Enter a number: "))
for j in range(1,11):
    print(i,"x",j,"=",(i*j))
