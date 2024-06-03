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
print(info)

#pop(): Removes the element with the specified key(delete a (key:value) pair)
# Syntax --> dict_name.pop("keyword")
info.pop("id")
info.pop("lab")
info.pop("result")
print(info)

# For nested --> dict_name["keyword"].pop("keyword")
info["contact"].pop("website")
print(info["contact"])

#clear(): Removes all the elements from the dictionary
info["contact"].clear()
print(info)
info.clear()
print(info)