# Q14. WAP using VSCode IDE. Use math library. Print number of options you have, when you are given 5 different characters and you need to select 3 of them without repeatitions. (find permutations)

import math

n = 5
r = 3

per =  math.factorial(n) // math.factorial(n-r)

print("There are total ",  per, "different types of ways to write the permutations.")








