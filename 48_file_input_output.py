# Write in a file:- [Syntax --> file.write("....")]
# opening moods for file write --> 1."w"   2."a"
# "w" --> overwrite previous all data/delete previous all data.
# "a"(append) --> add new data in file.But previous data are never lost.

f = open("Files for file input output/facebook.txt","w")
f.write("Facebook:\nFacebook is a social media platform with over 2.7 billion users.\nIt is one of the Big Five tech companies.\nFacebook has been criticized for its handling of misinformation.\nFacebook is a major player in the global technology market.")
f.close()

a = open("Files for file input output/facebook.txt","a")
a.write("\nThis is extra line.\nThank's a lot.")
a.close()

b = open("Files for file input output/twitter.txt","w")
b.write("Twitter:\nTwitter is a microblogging platform with over 440 million users.\nIt is one of the Big Five tech companies.\nTwitter has been criticized for its handling of misinformation.\nTwitter is a major player in the global technology market.")
b.close()