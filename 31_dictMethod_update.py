info = {
    "name" : "Anis",
    "semester" : "6th",
    "course" : ["ai","sd","cn","os"],
    "result" : {
        "1st" : 3.11,
        "2nd" : 3.20
    },
    "contact" :{
        "phone" : 880181835,
        "email" : "anis@gmail.com"
    },
    "child?" : False
}
print(info)

#update(): Updates the dictionary with the specified key-value pairs. Add a new pair of (key:value)
# Syntax --> dict_name.update({"keyword": "value"})
info.update({"id": 2314})
lab = ("ail","sdl","cnl","osl")
info.update({"lab": lab})
print(info)
# For nested --> dict_name["keyword"].update({"keyword": "value"})
info["result"].update({"3rd": 4.11})
info["contact"].update({"website": "www.anis512.com"})
print(info)