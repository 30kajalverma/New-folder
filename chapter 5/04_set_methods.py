s = {1 , 5 , 32 , 5 , 5, 5 , "Harry"} 

print(s, type(s))

#method 1
s.add(566)
print(s, type(s))
# for more method you can go for chatgpt
# properties of sets
# sets are unordered 
# sets are unindexed
# there is no way to change items in sets
# sets cannot contain duplicate values
s.remove(1)
print(s, type(s))
s.pop() #used to remove random element
print(s, type(s))