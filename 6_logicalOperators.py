'''
Logical Operators:
|| --> or
&& --> and
! --> not
'''
a = 5
b = 10
c = 15
# or --> if one comparison is "ture" , than it will true
print(a < b or a > c) # (a<b)=true or (a>c)=false --> true
print(a < b or a < c) # (a<b)=true or (a<c)=true --> true
print(a > b or a > c) # (a<b)=false or (a>c)=false --> false

# and --> if one comparison is "false" , than it will false
print(a < b and a > c) # (a<b)=true or (a>c)=false --> false
print(a < b and a < c) # (a<b)=true or (a<c)=true --> true
print(a > b and a > c) # (a<b)=false or (a>c)=false --> false

# not --> it give true for false and false for true
print(not(a < b or a > c)) # (a<b)=true or (a>c)=false --> true --> false
print(not(a < b or a < c)) # (a<b)=true or (a<c)=true --> true --> false
print(not(a > b or a > c)) # (a<b)=false or (a>c)=false --> false --> true