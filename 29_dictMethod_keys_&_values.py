info = {
    "name" : "Anis",
    "id" : 2314,
    "semester" : "6th",
    "course" : ["ai","sd","cn","os"],
    "lab" : ("ail","sdl","cnl","osl"),
    "result" : {
        "1st" : 3.11,
        "2nd" : 3.20
    },
    "contact" :{
        "phone" : 880181835,
        "email" : "anis@gmail.com",
        "website" : "www.anis512.com"
    },
    "child?" : False
}

#keys(): Returns a list containing the dictionary's keys
# Syntax --> list = dict_name.keys()
a = info.keys() #it's a list,but data type is: <class 'dict_keys'>
print(a, type(a))
# For nested dict --> list = dict_name["keyword"].keys()
b = info["result"].keys()
c = info["contact"].keys()
print(b)
print(c)

#values(): Returns a list of all the values in the dictionary
# Syntax --> list = dict_name.values()
d = info.values() #it's a list,but data type is: <class 'dict_keys'>
print(d, type(d))  # data type : <class 'dict_values'>
# For nested dict --> list = dict_name["keyword"].values()
e = info["result"].values()
f = info["contact"].values()
print(e)
print(f)