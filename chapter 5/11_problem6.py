#  ques 1 create an empty dictionary . Allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique
#  update isliye use kia kuki dusra rohan dla to nam to usne update kr dia
#  ques 2 if the names of 2 friends are same; what will happen to the program in problem 6
# ques 3 if two langauges are same
d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name:lang})

print(d)