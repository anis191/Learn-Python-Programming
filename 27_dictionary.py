# dictionary{} :-
# Dictionary is build-in data type in python
# Dictionary data type --> <class 'dict'>
# Dictionary store different types of data(int,float,string.bool,list,tuple,dict,set..)
'''
Dictionary Syntax -->
dictionary_name = {
    "keyword1" : "value1",
    "keyword2" : "value2",
    ..........,
    "keyword_n" : "value_n"
}
Nested Dictionary Syntax -->
dictionary_name = {
    "keyword1" : "value1",
    "keyword2" : "value2",
    "keyword3" : {
        "key1" : "value1",
        "key2" : "value2"
    }
}

Dictionary items are:-
1.Unorderd(No indexing)
2.changeable(change items,add items,remove items)
3.duplicate keyword/key not allowed
'''
# Create a dictionary{} -->
info = {
    "name" : "Anis",
    "Age" : 22,
    "Cgpa" : 3.12,
    "Is_adult" : True
}
print(info, type(info))

# Null/empty dictionary{} --> Syntax:- dictionary_name={}
em_dict = {}
print(em_dict, type(em_dict))

# Dictionary store different types of data(int,float,string.bool,list,tuple,dict,set..)
info = {
    "name" : "Anis",
    "id" : 2314,
    "gpa" : 3.33,
    "skills" : ["python","c","c++","java"],
    "num" : (1,2,3),
    "?" : True
}
print(info)