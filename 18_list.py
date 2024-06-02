# list[] :-
# List is build-in data type in python
# List data type --> <class 'list'>
# It is 90% similar to c/c++
# List store different types of data(int,float,string.bool,list..)
'''
List Syntax --> list_name = [item1, item2,....., item_n]
List Syntax --> list_name = list((item1, item2,....., item_n))

List items are:-
1.orderd(have indexing)
2.changeable(change items,add items,remove items)
3.allow duplicate items
'''
# Create a list[] -->
marks = [70,56,80,99,76]
print(marks)
print(type(marks))
# Null/empty list[] --> Syntax:- list_name=[]
null = []
print(null, type(null))

# List are orderd(have indexing) -->
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

#List items are changeable -->
marks[0] = 33 # list is changeable/mutable. That means if we are change any list item,it will be change the main list
print(marks)
name = ["anis","muhi","shariar"]
print(name)
name[1] = 'M'
print(name)

#List store different types of data(int,float,string.bool,list..)-->
list = ["Anis",2314,3.56,True,name]
print(list,type(list))
print(list[0], type(list[0]))
print(list[1], type(list[1]))
print(list[2], type(list[2]))
print(list[3], type(list[3]))
print(list[4], type(list[4]))

#***list[] slicing 100% same like string slicing