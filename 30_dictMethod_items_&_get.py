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

#items(): Returns a list containing a tuple for each key value pair, like (key:value)
# Syntax --> list = dict_name.items()
a = info.items()
print(a, type(a)) #data type: <class 'dict_items'>
# For nested dict --> list = dict_name["keyword"].items()
b = info["result"].items()
c = info["contact"].items()
print(b, "\n", c)

#get(): Returns the value of the specified key(same like normal dict value access)
# Syntax --> dict_name.get("keyword")
print(info.get("name"), type(info.get("name")))
print(info.get("id"), type(info.get("id")))
print(info.get("semester"), type(info.get("semester")))
print(info.get("course"), type(info.get("course")))
print(info.get("lab"), type(info.get("lab")))
print(info.get("result"), type(info.get("result")))
print(info.get("contact"), type(info.get("contact")))
print(info.get("child?"), type(info.get("child?")))

# Syntax --> dict_name["keyword"].get("keyword")
print(info["result"].get("1st"), type(info["result"].get("1st")))
print(info["result"].get("2nd"))
print(info["contact"].get("email"), type(info["contact"].get("email")))
print(info["contact"].get("phone"))
print(info["contact"].get("website"))