# syntax
# file = open('<file_name>','<modes>')
# <Operations>
# file.close()
# *******Or**********
# with open('<file_name>','<mode>') as file:
# <operations>

# Modes
# r -> read
# x -> create
# w -> write
# a -> append

# try:
#     file = open('data.txt', 'x')
#     file.close()
# except:
#     print("File already exists")

# with open('data.txt', 'r') as file:
#     x = file.read()
#     x = x.split('\n')

# n = int(input("enter n ="))
# a = x[n-1]
# print(a)

# to see sample pr read sample
# with open('data.txt', 'r') as file:
#     x = file.readline()
#     print(x)


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
# print(a)
# print("Grand Total")
# print(bill)
# with open('data.txt', 'a')as file:
#     file.write(a)


# *************Comma Seperated Value**************
# bill = 0
# n = int(input("Enter the number user = "))
# a = str()
# for i in range(n):
#     name = input("Enter product name = ")
#     price = float(input("Enter the price = "))
#     qty = int(input("Enter the quantity = "))
#     total = price * qty
#     a = a + f"{name},{price},{qty},{total}  \n"  # f is used for formatting
#     bill = bill + total
# print(a)
# print("Grand Total")
# print(bill)
# with open('data.csv', 'w')as file:
#     file.write('Name,Price,Quantity,Total\n')
#     file.write(a)

import os
try:
    os.remove('data.txt')
except:
    print("File does not exists")
import pandas as pd
df = pd.read_csv('data.csv')

print(df)
