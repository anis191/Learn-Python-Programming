#union(): (|)Return a set containing the union of sets
# Syntax --> set1.union(set2)
num1 = {1,3,5,6,7,9}
num2 = {1,2,3,4,5,8,10}
ans = num1.union(num2)
print(ans, type(ans))

f1 = {"mango","banana"}
f2 = {"apple","mango","lici"}
f = f1.union(f2)
print(f)

# Multiple set union --> new_set = set1 | set2 | set3 |....| set_n
a = {1,2,3}
b = {1,2,3,4,5}
c = {1,2,3,4,5,6,7}
d = {1,2,3,4,5,6,7,8,9}
new_set = a | b | c | d
print(new_set)

# intersection(): (&)Returns a set, that is the intersection of two other sets
# Syntax --> set1.intersection(set2)
num3 = {1,3,5,6,7,9}
num4 = {1,2,3,4,5,8,10}
ans2 = num3.intersection(num4)
print(ans2)

f3 = {"mango","banana"}
f4 = {"apple","mango","lici"}
new_f = f3.intersection(f4)
print(new_f)

# Multiple set intersection --> new_set = set1 & set2 & set3 &....& set_n
w = {1,3,5,6,8,9}
x = {1,3,5,7,8}
y = {2,3,5,6,8,9}
z = {2,3,4,5,6,7,8}
new = w & x & y & z
print(new)

#clear(): Removes all the elements from the set
p = {2,6,7,8,'a',"anis"}
print(p)
p.clear()
print(p)