# Applyable/usable for sequential data
# Syntax --> for variable in range/list/tuple/set:
list = [1,2,3,4,5]
tuple = ('A','B','C','D')
set = {"Anis","Rahim","Karim"}

for i in list:
    print(i)

for i in tuple:
    print(i)

for j in set:
    print(j)

# we can use (end='') for print all data in a single line. (end=' ') with a space
for a in list:
    print(a, end='')
print("\n")
for b in list:
    print(b, end=' ')
