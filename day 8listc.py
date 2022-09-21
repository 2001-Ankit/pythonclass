# pythoncollection
# list
# tuple
# dictionary
# set
# **********LIST*************
# List functions:
# indexing
# multiple data
# Duplicates
# Mutable

# a = [1, 2, 3, 4, 5]
# b = ['Apple', 'Ball', 'Cat', 'Dog', 'Eagle']
# # print(a)
# # print(type(a))
# # print(b)
# # print(type(b))
# # print(a[0])
# # print(len(a))
# # print(b[0:50:2])
# # c = ['Goat', 1, 2, 3]
# # d = b+c
# # print(d)
# # print(a*2)

# # User Defined List
l = []
s = 0
n = int(input("Enter the value of n ="))
for i in range(n):
    x = int(input("Enter a number = "))
    l = l.append(x)
    s = s + x
print("The maximum value of ", max(l))
print("The minimum value of ", min(l))
print("The sum =", sum(s))
l.sort()
print(l)
# l.reverse()
# print(l)


# b = ['Apple', 'Ball', 'Cat', 'Dog', 'Eagle']
# for i in b:
#     print(i)

# a1, a2 = [100, 200]
# print(a1)
# print(a2)

# b = ['Apple', 'Ball', 'Eagle', 'Cat', 'Dog', 'Eagle', 'Aeropale']
# if 'Apple' in b:
#     print("yes", b.count('Apple'))
# else:
#     print("NO")


# Function of list
# append()--> add the item in last in existing list
# insert()--> add in suitable index
# extend()-->add one list in another list

# b.append('Ankit')
# print(b)

# b.insert(1, 'Ankit')
# print(b)

# a = [1, 2, 3, 4, 5]
# b.extend(a)
# print(b)

# a = [1, 2, 3, 4, 5]
# a[0:3] = 'Ankit', 'Ball', 'Cat'
# print(a)
# del a[0:3]
# print(a)
# a.remove('Ankit')
# print(a)

# b = a.pop(1)
# print(a)
# print(b)
# l = len(a)
# for i in range(l):
#     if a[i] == 3:
#         print(i)
# Assignment
a = ['Apple', 'Ant', 'Ball', 'Zebra', 'Cat']
b = 'ant'
for b in a:
    if b.lower() == 'Ant'.lower():
        print("Yes")
    else:
        print("No")
