fruit = "Mango"
# We need to slicing this string from (M) to (g):
# Syntax --> string_name(starting_index : ending(n_th)character)
print(fruit[0 : 4]) #It was slice the string from 0th index to 4th character
# ***It did not change the main string.Just copy the string and than do slice operation
print(fruit)

# Now we need to slice the fruit string from (a) to (g):
'''
In this fruit string the indexing is--> 
fruit[0] = M and character no = 1
fruit[1] = a and character no = 2
fruit[2] = n and character no = 3
fruit[3] = g and character no = 4
fruit[4] = o and character no = 5
We need to slice (a) to (g):-
Now what is the index no of (a)? ans:[1]
what is the character no of (g)? ans:[4]
'''
print(fruit[1 : 4])

#If we do not mention the starting index, than python automatic slice from 0th index
print(fruit[ : 3]) #It was automatically slice from 0th index to 3rd character

#If we do not mention starting index and ending character,than it automatically print full string
print(fruit[ : ])

#Negetive Slicing:
print(fruit[0 : -1]) #It was slice the string from 0th index to (len(fruit)-1)_th character

print(fruit[-3 : -1]) #It was slice the string from (len(fruit)-3) no index index to (len(fruit)-1)_th character