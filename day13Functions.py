# Function are of two types
# Pre defined ->print() input() int() float() str()
# User defined
#  Syntax
# def <function_name>():
#     <operations>

# <function_name>()

# function without agruments and non return type

# def ankit():
#     print("Hello")


# ankit()

# def area():
#     l = int(input("Enter length:")) --> local variable
#     b = int(input("Enter breadth: ")) --> local variable
#     a = l * b
#     print(a)


# area()


# Global variable
# l = 10
# b = 2


# def area():
#     a = l * b
#     print(a)


# area()
# Using local as global

# def area():
#     global l, b
#     l = 10
#     b = 2
#     a = l*b
#     print(a)


# area()
# print(l, b)


# Types of function
# function without agruments and non return type
# function with agruments and non return type
# function without agruments and return type
# function with agruments and return type


# function with agruments and non return type
# def area(l, b):  # Parameter
#     a = l * b
#     print(a)


# l = int(input("ENter len"))
# b = int(input("Enter breadth"))
# area(l, b)  # Argument


# def area(x, y):  # Parameter
#     a = x * y
#     print(a)


# l = int(input("ENter len"))
# b = int(input("Enter breadth"))
# area(l, b)  # Argument

# def area(x, y):
#     a = x * y
#     print(a)


# def vol(x, y, z):
#     v = x * y*z
#     print(v)


# l = int(input("Enter a length"))
# b = int(input("Enter a breadth"))
# h = int(input("Enter a height"))


# area(l, b)
# vol(l, b, h)

# Default value


# def language(lan="Python"):
#     print(lan)


# language("c")
# language("C++")
# language("R")
# language()

# Return Type function
# def hello():
#     return"Hello World"


# print(hello())

# def area():
#     l = 20
#     b = 2
#     a = l*b
#     return a


# ar = area()
# h = 2
# v = ar*h
# print("The area =", ar)
# print("The volume =", v)

# def cal(x):
#     l, b, h = x
#     a = l*b
#     v = a*h
#     return a, v


# l = int(input("Enter l ="))
# b = int(input("Enter a breadth"))
# h = int(input("Enter a height"))
# data = (l, b, h)
# av = cal(data)
# print(av)
# ar, vol = av
# print("the area =", ar)
# print("the vol =", vol)


# Revursice Function
# def hello():
#     print("Hello")
#     x = input("Enter y for more print")
#     if x == 'y':
#         hello()


# hello()

bill = 0
s = str()


def bill():
    global s
    name = input("Enter product name = ")
    price = float(input("Enter the price = "))
    qty = int(input("Enter the quantity = "))
    total = price * qty
    s = s + f"{name}  {price}  {qty}  \n"

    bill = bill + total
    bill()


bill()
print(s)
