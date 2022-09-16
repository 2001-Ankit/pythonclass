# Syntax
# if <condition>:
#     <operation>
# elif<condition>:
#     <operation>
# .....
# else:
#     <operation>


# Example:
# a= input("Enter your name = ")
# if a =="ankit":
#      print("yes")
# elif a!="ankit":
#      print("no")
# else:
#     print("Wrong name")

# Greater than or not
# a= int(input("Enter a ="))
# b= int(input("Enter b= "))
# if a>b:
#     print("A is greater than B")
# elif a<b:
#     print("A is less than B")
# elif a == b:
#     print("Equal")
# Boolean
# a = 15
# b = 14
# print(a<b)

# ODD and Even
# a = int(input("Enter a number = "))
# if a%2 == 0:
#     print(a,"even")
# else:
#     print(a,"odd")
# Assignment : Write a program to enter all marks of subjects of student find total marks
# find the grade of total marks
name = input("Enter your name = ")
p = int(input("Enter your marks of Physics = "))
c = int(input("Enter your marks of Chemistry = "))
m = int(input("Enter your marks of Maths = "))
e = int(input("Enter your marks of English = "))
T = p + c + m + e
print("Total =", T)
per = (T)/4
if (per >= 80):
    print("Distinction")
elif (per >= 70 and per < 80):
    print("First Division")
elif (per >= 60 and per < 70):
    print("Second Division")
elif (per >= 50 and per < 60):
    print("Third Division")
else:
    print("Failed")
