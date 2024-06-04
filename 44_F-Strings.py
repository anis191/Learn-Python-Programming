#To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions.
# Syntax -->
# string_name = f" .........{variable/operators..}....."
name = "Karim"
st = f"Hi,{name} welcome to our website!"
print(st)

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Your city: ")
sport = input("Favourite sport: ")

out = f"Hey, I am {name}.\nI'm {age} years old.\nI live in {city}.\nMy favourite soprt is {sport}"
print(out)

a = 10
b = 7
c = f"Sum is {a+b}. Sub is {a-b}. Mul is {a*b}. Div is {(a/b):.3f}"
print(c)

fruit = "mango"
print(f"This is a {fruit.upper()}")