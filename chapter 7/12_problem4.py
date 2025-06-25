# write a program to find whether a given number is prime or not.

# User se number input le rahe ho.
n = int(input("Enter a number: "))

# Loop start ho raha hai 2 se le kar n-1 tak
for i in range(2,n):

# 10 % 2 → 0     ✅ (10 perfectly divides by 2)
# 10 % 3 → 1     ❌ (10 not fully divisible by 3)
    if(n%i) == 0:
        print("Number is not prime") #Jaise hi number divide ho gaya Program break kar deta hai → loop ko rokh deta haiAur bol deta hai → "Number is not prime"
        break
else:     #Agar for loop kabhi bhi break nahi hua, tab ye else chalega
    print("Number is prime")