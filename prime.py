# Prime Number : Number which is divisible by itself and one
# If the number is divisible by any other number, other thatn 1 and itself
# divisible --> remainder is 0

num = int(input("Enter the number here : "))

# n=2
# while(n<num):
#     if(num%n==0):
#         print("Not Prime number")
#         break
#     print("Prime")
#     n+=1

n=2
while(n<num):
    if(num<2):
        print("Not a Prime")
    elif(num%n==0):
        print("Not a prime")
        break
    n=n+1
else:
    print("Prime")














