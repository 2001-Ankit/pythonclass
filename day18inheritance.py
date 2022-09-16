# class A:
#     pass


# class B(A):  # Here class A is inherited
#     pass


# obj = B()

# class Data:
#     def __init__(self, add):
#         self.add = add


# class Info(Data):
#     def __init__(self, name, adds):
#         self.name = name
#         Data.__init__(self, add)

#     def info(self):
#         print(f"Hello world i am{self.name}.I am from{self.add}")


# name = input("ENter your name")
# add = input("ENter input address")
# obj = Info(name, add)
# print(obj.info())


# Multiple inheritance or multilevel inheritance


# class A:
#     pass


# class B(A):
#     pass


# class C(B):
#     pass


# obj = C()


# Example of Multilevel Inheritance
# class A:
#     def __init__(self, age):
#         self.age = age


# class Data:
#     def __init__(self, age, add):
#         self.add = add
#         A.__init__(self, age)


# class Info(Data):
#     def __init__(self, name, age, add):
#         self.name = name
#         Data.__init__(self, age, add)

#     def info(self):
#         print(
#             f"Hello World I am {self.name}.I am {self.age}.I am from {self.add}")


# name = input("Enter your name")
# age = int(input("ENter age"))
# add = input("Enter address")
# obj = Info(name, age, add)
# print(obj.info())
# if one error occur in a level whole program is error


# Multiple Inheritance
# class A:
#     def __init__(self, age):
#         self.age = age


# class Data:
#     def __init__(self, add):
#         self.add = add


# class Info(A, Data):
#     def __init__(self, name, age, add):
#         self.name = name
#         Data.__init__(self, add)
#         A.__init__(self, age)

#     def info(self):
#         print(
#             f"Hello World I am {self.name}.I am {self.age}.I am from {self.add}")


# name = input("Enter your name")
# age = int(input("ENter age"))
# add = input("Enter address")
# obj = Info(name, age, add)
# print(obj.info())


# Public Member
# class Info:
#     def __init__(self, name, age, add):
#         self.name = name
#         self.age = age
#         self.add = add


# obj = Info("Ram", 45, "Kathmandu")
# print(obj.name)
# print(obj.age)
# print(obj.add)


# Protected Member
# class Info:
#     def __init__(self, name, age, add):
#         self.__name = name
#         self.__age = age
#         self.__add = add


# obj = Info("Ram", 45, "Kathmandu")
# print(obj.name)
# print(obj.age)
# print(obj.add)


# # Private member (__)
# class Info:
#     def __init__(self, name, age, add):
#         self._name = name
#         self._age = age
#         self._add = add


# obj = Info("Ram", 45, "Kathmandu")
# print(obj.name)
# print(obj.age)
# print(obj.add)
