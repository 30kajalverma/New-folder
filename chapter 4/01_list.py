# kisi bi programming language m agr apko bhaut sare same elements ko store krna h to list istemal krte ho 
# you can change string in case of list
friends = ["Apple", "Orange", 5 , 345.06, False , "Akash", "Saiyam"]

print(friends[0])
friends[0] = "Grapes"

print(friends[0]) #unlike strings lists are mutable
# index whi string ki tarah 0 se start hoti h 

# jaise ki hum string ki slicing kr skte h waise in hum list ki b kr skte h
print(friends[1:4])
