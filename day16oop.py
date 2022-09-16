# **************OOP************
# Class, Object and Methods
# class:
# A class is a blueprint for the object
# class Python:
#     pass
# Syntax
# class <class_name>:
#     <operations>

# obj = <class_name>


# Example
# class Hello:  # Class
#     def hello(self):  # Method or may be function which can be one or many
#         print("Hello World")


# obj = Hello()  # obj
# obj.hello()


# class Cal:
#     def cal(self):
#         l = int(input("Enter l ="))
#         b = int(input("Enter b ="))
#         h = int(input("Enter h ="))
#         a = l*b
#         v = a*h
#         print("The area = ", a)
#         print("The volume = ", v)


# obj = Cal()
# obj.cal()


# self parameter
# It is a reference to the current instance of the class
# class Cal:
#     @staticmethod
#     def cal(l, b, h):
#         a = l * b
#         v = a * h
#         print("The area =", a)
#         print("The volume =", v)


# l = int(input("Enter  length ="))
# b = int(input("Enter  breadth ="))
# h = int(input("Enter  height ="))
# obj = Cal()
# obj.cal(l, b, h)


# Passing arguments
# class Cal:
#     def cal(self, l, b, h):
#         a = l * b
#         v = a * h
#         print("The area =", a)
#         print("The Volume = ", v)


# l = int(input("ENter l = "))
# b = int(input("Enter b ="))
# h = int(input("Enter h ="))
# obj = Cal()
# obj.cal(l, b, h)

# WIith different function in a class
# class Cal:
#     def area(self, x, y):
#         a = x*y
#         print("The area =", a)

#     def volume(self, x, y, z):
#         v = x * y * z
#         print(v)


# l = int(input("ENter l = "))
# b = int(input("Enter b ="))
# h = int(input("Enter h ="))
# obj = Cal()
# obj.area(l, b)
# obj.volume(l, b, h)


# Using __init__() function
# class Cal:
#     def __init__(self, x, y, z):
#         self.a = x
#         self.b = y
#         self.c = z

#     def area(self):
#         ar = self.a * self.b
#         print("area =", ar)

#     def vol(self):
#         v = self.a*self.b*self.c
#         print("Volume = ", v)


# l = int(input("Enter length ="))
# b = int(input("Enter breadth ="))
# h = int(input("Enter height ="))
# obj = Cal(l, b, h)
# obj.area()
# obj.vol()


class Info:
    def __init__(self, name, age, add):
        self.n = name
        self.a = age
        self.ad = add

    def myInfo(self):
        print(
            f"Hello World my name is {self.n} and i am {self.a} years old.I live in {self.ad}")


name = input("Enter your name :")
age = input("Enter your age:")
add = input("Enter your address:")

obj = Info(name, age, add)
obj.myInfo()
print(obj.n, obj.a, obj.ad)
