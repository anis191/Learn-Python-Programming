# tuple() :-
# Tuple is build-in data type in python
# Tuple data type --> <class 'tuple'>
# It is 90% similar to list
# Tuple store different types of data(int,float,string.bool,list,tuple..)
'''
Tuple Syntax --> tuple_name = (item1, item2,....., item_n)
Tuple Syntax --> tuple_name = tuple((item1, item2,....., item_n))

Tuple items are:-
1.orderd(have indexing)
2.Unchangeable(can't change items,can't add items,can'tremove items)
3.allow duplicate items
'''
# Create a tuple() -->
marks = (70,56,80,99,76)
print(marks)
print(type(marks))
# Null/empty tuple() --> Syntax:- tuple_name=()
null_tuple = ()
print(null_tuple, type(null_tuple))

# Tuple are orderd(have indexing) -->
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

#Tuple items are Unchangeable -->
# marks[0] = 33 --> It's wrong,because tuple items is unchangeable
name = ("anis","muhi","shariar")
print(name, type(name))
# name[1] = 'M' --> It's wrong,because tuple items is unchangeable

name2 = ["anis","muhi","shariar"]

# Tuple store different types of data(int,float,string.bool,list..)-->
tuple = ("Anis",2314,3.56,True,name,name2)
print(tuple,type(tuple))
print(tuple[0], type(tuple[0]))
print(tuple[1], type(tuple[1]))
print(tuple[2], type(tuple[2]))
print(tuple[3], type(tuple[3]))
print(tuple[4], type(tuple[4]))
print(tuple[5], type(tuple[5]))

# One value tuple:
# Syntax --> tuple_name=(4,) ***Use comma after value/element
new = (5,)
print(new, type(new))