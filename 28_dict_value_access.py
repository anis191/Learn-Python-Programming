# We can access any dictionary items/elements using it's keyword/key
# For nested dictionary --> dictionary_name["keyword"]["keyword"]
info = {
    "name" : "Anis",
    "id" : 2314,
    "semester" : "6th",
    "course" : ["ai","sd","cn","os"],
    "lab" : ("ail","sdl","cnl","osl"),
    "result" : {
        "1st sem" : 3.11,
        "2nd sem" : 3.20
    },
    "child?" : False
}

# Syntax --> dictionary_name["keyword"]
print(info["name"], type(info["name"]))
print(info["id"], type(info["id"]))
print(info["semester"], type(info["semester"]))
print(info["course"], type(info["course"]))
print(info["lab"], type(info["lab"]))
print(info["result"], type(info["result"]))
print(info["child?"], type(info["child?"]))

# For nested dictionary --> dictionary_name["keyword"]["keyword"]
print(info["result"]["1st sem"])
print(info["result"]["2nd sem"])

# Dictionary items are changeable:
# Syntax --> dictionary_name["keyword"] = "new value"
info["name"] = "Karim"
info["id"] = 3012
print(info)

# For nested --> dictionary_name["keyword"]["keyword"] = "new value"
info["result"]["1st sem"] = 4.11
info["result"]["2nd sem"] = 4.99
print(info)