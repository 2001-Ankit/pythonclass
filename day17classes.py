

# class Area:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area(self):
#         a = self.x * self.y
#         print(a)


# class Volume:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def vol(self):
#         v = self.x*self.y*self.z
#         print(v)


# l = int(input("Enter length = "))
# b = int(input("Enter breadth = "))
# h = int(input("Enter height = "))
# obj = Area(l, b)
# obj1 = Volume(l, b, h)
# obj.area()
# obj1.vol()

# __str__ method->string representation of a certain class
# class Info:
#     def __init__(self, name, age, add):
#         self.name = name
#         self.age = age
#         self.add = add

#     def __str__(self):
#         return self.name


# name = input("Enter a name =")
# age = int(input("Enter age = "))
# add = input("Enter a address")

# obj = Info(name, age, add)
# print(obj)
# print(str(obj))


# Operator Overloading
class Total:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        x = self.x+other.x
        return Total(x)


obj = Total(1000)
obj1 = Total(2000)
print(obj+obj1)
print(obj)
print(obj1)
