# string : jo b quotes m likhe
# string is immutable agr m suppose harry m se r ko replace krna chahu to m nhi kr skti

a = "harry"
b='harry'
c= '''harry'''

# string slicing
name = "Harry"
#  H   A    R     R    Y
#    0   1    2     3    4 POSITIVE SLICING
    # -5  -4   -3    -2   -1 NEGATIVE SLICING
nameshort = name[0:3] #start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)