# if elif else ladder

a = int(input("Enter your age: "))

if(a>=18):
    print("you are above the age of consent")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):   
    print("You are entering 0 which is not a valid age")
    

else:
    print("You are below the age of consent")

print("End of program")

# for logical operators u can go for chat gpt
# and 
# or 
# not
# and =>
# if age > 18 and age < 60:
#     print("Adult")

# or=>
# city = input("Enter city name: ")

# if city == "Delhi" or city == "Mumbai":
#     print("Big City")

#not
# 🔁 True → False
# 🔁 False → True

# raining = False

# if not raining:
#     print("Let's go outside!")

