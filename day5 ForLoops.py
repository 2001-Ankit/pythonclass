# multiple time executions
# Types of loops
# 1.for loop --> n number of types,uses range function-->sequence of number
# 2.while loop -->
# for i in range(1, 5):
#     print(i, "hello world")
# for j in range(1, 5):
#     print("ankit")


# multiplication table
# n = int(input("Enter the number = "))
# for i in range(1, 11):
#     print(n, "*", i, "=", n*i)
# Phone Diary
# a = str()
# n = int(input("Enter a number ="))
# for i in range(n):
#     s = input("Enter your name = ")
#     x = int(input("ENter phone number for X ="))
#     a = a+s+" "+str(x)+"\n"
# print(a)


# Factorial
# fac = 1
# n = int(input("enter n = "))
# for i in range(1, n+1):
#     fac = fac * i
#     print(fac)


# Assignment
# WAP to create a billing taking data from user like (product name price and quantity)


bill = 0
n = int(input("Enter the number user = "))
a = str()
for i in range(n):
    name = input("Enter product name = ")
    price = float(input("Enter the price = "))
    qty = int(input("Enter the quantity = "))
    total = price * qty
    a = a + name+" " + str(price) + " " + str(qty) + "\n"
    bill = bill + total
print(a)
print("Grand Total")
print(bill)
