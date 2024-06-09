'''
1.Length:-Most smallest email like "a@b.in".Here length is --> 6
==> So, we need to check length is greather than or equal(>=) to 6 
2.Email always start with lower letter character.
==> So, we need to check 1st character is a lower letter alphabet or not.
3.Email must have a "@", just 1 time in a email.
==> So, we need to check "@" is exist or not, and how many times.
4.Email must have a "."(dot), before "com" or "in"(.com/ .in)
==> So, we need to check dot(.) in -4th or -2th position
5.Email have no captal/upper case alphabet, special character except(_/./@).And using digit in email is valid.
==>
'''
email = input("Enter Your Email: ")
wrong = 0
if(len(email) >= 6):
    if(ord(email[0]) >= 97 and ord(email[0]) <= 122):
        if(email.find('@') != -1) and (email.count('@') == 1):
            if((email[-4] == '.') ^ (email[-3] == '.')):
                for i in email:
                    if(ord(i)>= 65 and ord(i)<= 90):
                        wrong = 1
                        break
                    elif(ord(i)>=97 and ord(i)<=122):
                        continue
                    elif(ord(i) >= 48 and ord(i) <= 57):
                        continue
                    elif(i=='_' or i=='.' or i=='@'):
                        continue
                    else:
                        wrong = 1
                        break
                if(wrong == 1):
                    print("Wrong Email!")
                else:
                    print(email)
            else:
                print("Please enter dot(.), before \"com\" / \"in\" !")
        else:
            print("Please enter '@', just one time!")
    else:
        print("Please start with lower case alphabet")
else:
    print("Enter 6 or more characters!")