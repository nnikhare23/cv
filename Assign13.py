# Q13.WAP using VSCode IDE.  Import math library and print the gcd, lcm of two numbers.

import math

num1 = int(input("Enter the first number here : "))
num2 = int(input("Enter the second number here : "))

#HCF 
if(num1>num2):
    max = num1
else:
    max = num2

for i in range(1, max+1):
    if(num1%i==0 and num2%i==0):
        hcf=i

print("HCF of two number is ", hcf)


# LCM
while(True):
    if(max%num1==0 and max%num2==0):
        break
    max = max + 1

print("The LCM of two number is ", max)






























