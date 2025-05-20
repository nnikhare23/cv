
# 1.	A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
# Take following input from user Number of classes held Number of classes attended. And print percentage of class attended  
# Is student is allowed to sit in exam or not.


# class_held = int(input("Enter classes held "))
# class_attended = int(input("Enter class attended"))

# percentage = (class_attended/class_held)*100
# print("The Percentage of student which will attended the class is ", percentage)

# if(percentage>=75):
#     print("Student is allowed to attended the exam")
# else:
#     print("Student is not allowed to attenede the exam")






# 2. Modify the above question Q1. if student has attendance less than 75% then ask user if he/she has medical cause or not ( 'Y' or 'N' ).  
# print "Allow" if he/she has medical cause else not allowed. 


# class_held = int(input("Enter classes held "))
# class_attended = int(input("Enter class attended"))

# percentage = (class_attended/class_held)*100
# print("The Percentage of student which will attended the class is ", percentage)

# if(percentage>=75):
#     print("Student is allowed to attended the exam")
# else:
#     medical_cause = str(input("Enter medical cause in Yes or Not"))
#     if(medical_cause=="Yes"):
#         print("You are allowed to attend the exam")
#     elif(medical_cause=="Not"):
#         print("You are not allowed to attend the exam")







# 3. Take a number from user. Print whether it is even number or odd number.
        
# num = int(input("Enter the number here : "))

# if(num%2==0):
#     print("Even number")
# else:
#     print("Odd Number")



# 4.	A school has following rules for grading system:  
# a.	Below 25 - F  
# b.	25 to 45 - E  
# c.	45 to 50 - D  
# d.	50 to 60 - C  
# e.	60 to 80 - B  
# f.	Above 80 - A  
# Ask user to enter marks and print the corresponding grade. 


# print("Select grade : 1. Below 25, 2. Between 25 to 45, 3. between 45 t0 50, 4. between 50 to 60, 5. between 60 to 80, 6. Above 80")

# grade = int(input("Enter the grade here : "))

# if(grade<=25):
#     print("Fail and Grade is F")
# elif(grade>25 and grade<=45):
#     print("Grade is E")
# elif(grade>45 and grade<=50):
#     print("Grade is D")
# elif(grade>50 and grade<=60):
#     print("Grade is C")
# elif(grade>60 and grade<=80):
#     print("Grade is B")
# elif(grade>80):
#     print("Grade is A")




# 6. Accept number from user and check whether it is divisible by 5 and 11 if divisible then display appropriate message.  

# num = int(input("Enter the number for checking it divisible by 5 and 11"))

# if(num%5==0 and num%11==0):
#     print("Number ", num, "is divisible by 5 and 11")
# else:
#     print("Number is not divisible by both")




# 7. Write a program to take a number from user. Check whether the last digit of that is divisible by 3 or not.  
# [hint: last digit of num is num%10]

# num = int(input("Enter the number here : "))
# last_digit = num%10

# if(last_digit%3==0 and last_digit!=0):
#     print("Last digit of the number is divisible by 3")
# else:
#     print("Last digit of number is not divisible by 3")



# 8.	Write a program to check whether an years is leap year or not the year is leap if it satisfies following condition  
# •	It the year is divisible by 100 o If it is divisible by 100, then it should also be divisible by 400 then it is leap year  
# •	otherwise, all other years divisible by 4 and not divisible by 100 then it is leap year.





