
# Yeh ek list hai jisme alag-alag type ke items hain:
# Number: 1
# String: "Harry", "This"...
# Boolean: False

l = [1, "Harry", False , "This", "Rohan", "Shubham", "Shubhi"]

# i list ke index ko track karega. Shuruaat me 0 rakha gaya hai (kyunki list indexing 0 se shuru hoti hai).

i = 0

# len(l) ka matlab list me kitne items hain. Is list me 7 items hain.
# Lekin yaha len(l) + 1 likha hai, matlab: while(i < 8) chalega.
# Index i 0 se 7 tak jayega.
# Lekin list me sirf 0 se 6 tak hi elements hain.
# Jab i = 7 hoga, to l[7] likhne par error aayega kyunki list me index 7 ka koi element hi nahi hai!

while(i<len(l)):
    print(l[i])
    i +=1