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

#copy(): Returns a copy of the dictionary
new_info = info.copy()
print(new_info)

new_result = info["result"].copy()
new_contact = info["contact"].copy()
print(new_result)
print(new_contact)