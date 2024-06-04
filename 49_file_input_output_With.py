# Syntax -->
'''
with open("file_name","mode") as variable:
    read()/write().....
*** it automatically close file.
'''
with open("Files for file input output/twitter.txt","r") as f:
    a = f.read()
    print(a)

LinkedIn = '''LinkedIn:
LinkedIn is a professional networking platform with over 700 million users.
It is owned by Microsoft.
LinkedIn supports climate action initiatives.
LinkedIn is a major player in the global technology market.'''

with open("Files for file input output/linkedin.txt","w") as a:
    a.write(LinkedIn)

Netflix = '''
Netflix:
Netflix is a streaming service with over 247 million paid memberships.
It is a leading provider of streaming services globally.
Netflix supports climate action initiatives.
Netflix is a major player in the global technology market.
'''
with open("Files for file input output/linkedin.txt","a") as b:
    b.write("\nAdd Netflix -->")
    b.write(Netflix)
