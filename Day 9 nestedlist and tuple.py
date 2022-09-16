# nested list of list inside list
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# # print(a)
# print(a[0][1])

# a = [['Ram', 45, 'Usa'], ['Ram', 45, 'Usa'], ['Ram', 45, 'Usa']]
# # print(a)
# for i in a:
#     print(i)
# data = []
# n = int(input("Enter the n = "))
# for i in range(n):
#     name = input("ENter your name")
#     age = int(input("Enter your age"))
#     add = input("Enter your address = ")
#     data.append([name, age, add])
# print(data)

# a = [['Ankit', 21, 'USA'], ['Seemon', 21, 'USA']]
# name = input("ENter name")
# for i in a:
#     if name in i:
#         print(i)
#     else:
#         print("No")
# a = [['Ankit', 21, 'USA'], ['Seemon', 21, 'USA']]
# name = input("ENter name")
# for i in range(len(a)):
#     if name in a[i]:
#         print(i)


# bill = 0
# n = int(input("Enter the number user = "))
# a = str()
# for i in range(n):
#     name = input("Enter product name = ")
#     price = float(input("Enter the price = "))
#     qty = int(input("Enter the quantity = "))
#     total = price * qty
#     a = a + f"{name}  {price}  {qty}  \n"  # f is used for formatting
#     bill = bill + total
# # print(a)
# # print("Grand Total")
# # print(bill)
# x = a.split('\n')[0:-1]
# bill = []
# for i in x:
#     y = i.split()
#     bill.append(y)
# print(bill)


# *******************************************TUPLE***************************************
# ->Ordered
# ->Indexing
# ->Duplicate Value
# ->Multiple value
# ->Imutable
# no append() insert() extend()
# no del remove
# t = tuple()
# t = (1, 2, 3, 4)
# r = ("Apple", "Ball", "Cat")
# print(r)
# print(type(r))
# r = ("Apple",)
# print(type(r))
# WAP to display tuple
# n = int(input("Enter a number"))
# data = tuple()
# for i in range(n):
#     x = int(input("Enter a value"))
#     data = data + (x,)
# print(data)
