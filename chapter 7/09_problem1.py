# write a program to print multiplication table of a given number using for loop.


# input(): User se number mangta hai (jaise: 5)
# int(): Us input ko integer (number) me badalta hai
#  Agar tumne "5" type kiya, to wo string hota hai → int("5") se number 5 ban jata hai
# Ab n me user ka number store ho gaya
n = int(input("Enter a number: "))

# Yeh for loop 1 se 10 tak chalega
# range(1, 11) ka matlab

for i in range(1, 11):

    
# Yeh line har i ke liye n ka multiplication print karegi
# f"{...}" ek formatted string hoti hai, jisme variables seedha print ho jaate hain. f string ki help se ap variable ka b prayoog kr skte h.
# {n*i} ka matlab hai: number n ko i se multiply karo


    print(f"{n} x {i}) = {n*i}")