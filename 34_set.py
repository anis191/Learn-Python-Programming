# set{} :-
# set is build-in data type in python
# set data type --> <class 'set'>
# It is 80% similar to tuple
# set store different types of data(int,float,string.bool,tuple..)
# set cannot store list and dictionary, because they are changeable.
'''
set Syntax --> set_name = {item1, item2,....., item_n}
set Syntax --> set_name = set((item1, item2,....., item_n))

set items are:-
1.Unorderd(No indexing)
2.Unchangeable(can't change items)
    --> But add new items and also removes items
3.duplicate items not allowed
'''
# Create a set{} -->
num = {1,2,3,4,5}
print(num)
print(type(num))
c = {1,2,3,"hello","world"}
print(c)
# Null/empty set{} --> Syntax:- set_name = set()
empty_set = set()
print(empty_set, type(empty_set))