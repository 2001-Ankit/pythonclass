# class Info:
#     def __init__(self, name, age, add):
#         self.name = name
#         self.age = age
#         self.add = add

#     def __str__(self):
#         return str(self.age)


# name = input("Enter your name:")
# age = int(input("Enter age:"))
# add = input("Enter address:")

# obj = Info(name, age, add)
# print(obj)
# print(obj.__str__())
# print(str(obj))

class Total:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        x = self.x + other.x
        return Total(x)


obj = Total(1000)
obj1 = Total(1220)
obj2 = Total(6000)
print(obj+obj1+obj2)
print(obj)
print(obj1)
print(obj2)
