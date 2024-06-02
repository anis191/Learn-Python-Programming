# 1.upper():Converts a string into upper case
# Syntax --> x = string.upper()
a = "Anisul alam"
u = a.upper() #It can't change main string,that's why we need to store this new upper string in another string
print(u)
#We also convert a single character in lower to upper using upper()
print(a[1].upper())
c = 'd'
print(c.upper())

print(a) #It can't change main string.That's why here the main string is still unchanged

# 2. All are same it just convert upper to lower
b = "HELLO WORLD"
print(b.lower())
print(b[3].lower())