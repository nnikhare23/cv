# Q15. WAP using VSCode IDE. Use math library. Print number of options you have to select 20 students out of 60 without repeatitions. ( Obviously here order doesn't matter, so find combinations)

import math

total_student = 60
select = 20

# First way to find combination without using any functions
# The formula for find this combinations is com = fac(n)//(fact(k)*fact(n-k))
combination = math.factorial(total_student) // (math.factorial(select) * math.factorial(total_student - select))   

#Second way to find is using the math.comb lib use
# combinations = math.comb(total_student, select)

print("The different ways of 20 students combinations from 20 students is ", combination)









