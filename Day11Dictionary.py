# Dictionary
# ->Indexing
# ->Ordered
# ->Mutable
# ->Multiple and duplicate data

# d = {}
# e = dict()
# print(type(d))
# print(type(e))

# Syntax
# d = {<key>:<Value>,<key>:<Value>}
# d = {'a': 'Ankit', 'b': 'ball', 'c': 'Cat'}
# e = {1: 1, 2: 4, 3: 9}
# print(e, d)
# print(type(d), type(e))

# print(d['a'])

# a = {}
# a['a'] = 'Apple'
# a['b'] = 'Ball'
# a['c'] = 'Cat'
# print(a)

# Creating a dictionary
# a = {}
# n = int(input("ENter the value of n"))
# for i in range(n):
#     name = input("ENter name")
#     phone = int(input("Enter phone"))
#     key = name
#     value = phone
#     a[key] = value
# print(a)

# Reading from dictionary
# d = {'Ankit': 9813928960, 'Seemon': 9864266947,
#  'Namrata': 9849707637, 'Sita': 9841928905}
# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

# l = []
# for i in d.items:
#     l.append(i)

# print(l)

# we can use del or pop() to delete from dictionary
# d = {'Ram': [981392896], 'Shyam': [9864266947]}
# print(d, "List inside dictionary")
# a = {}
# n = int(input("ENter the value of n"))
# for i in range(n):
#     name = input("ENter name")
#     ntc_phone = int(input("Enter phone"))
#     ncell_phone = int(input("Enter phone"))
#     a[name] = [ntc_phone, ncell_phone]

# print(a)

# d = {'name': [], 'age': [], 'add': []}
# n = int(input("ENter a number"))
# for i in range(n):
#     name = input("ENter your name")
#     age = int(input("Enter your age"))
#     add = input("ENter your address")
#     d['name'].append(name)
#     d['age'].append(age)
#     d['add'].append(add)

# print(d)

# Changing data in dict


# d = {'name': ['Ankit', 'Seemon'], 'age': [21, 22], 'add': ['USA', 'Nepal']}
# d['add'][0] = 'nepal'
# print(d)

# Deleting
# del d['name'][0]
# del d['age'][0]
# del d['add'][0]
# print(d)

# WAP to create dict inside list and perform CRUD
# a = [{'name': 'Ram', 'age': 45, 'add': 'Kathmandu'},
#      {'name': 'Shyam', 'age': 75, 'add': 'Bhaktapur'},
#      {'name': 'Nabin', 'age': 54, 'add': 'Lalitpur'}]

# nested dictionary
# d = {1: {'name': 'Ram', 'age': 10, 'grade': 'A'},
#      2: {'name': 'Am', 'age': 11, 'grade': 'C'},
#      3: {'name': 'Sam', ' age': 12, 'grade': 'B'}}


# a = [{'name': 'Ram', 'age': 45, 'add': 'Kathmandu'},
#      {'name': 'Shyam', 'age': 75, 'add': 'Bhaktapur'},
#      {'name': 'Nabin', 'age': 54, 'add': 'Lalitpur'}]


# a = list()
# n = int(input("Enter a number"))
# for i in range(n):
#     name = input("Enter your name")
#     age = int(input("Enter your age"))
#     add = input("Enter your address")
#     a.append({'name': name, 'age': age, 'add': add})
# print(a)
# for i in a:
#     print(i)

# for i in a:
#     del a[-1]
#     print(a)

# for i in a:
#     a[0] = {'name': 'Ankit', 'age': 21, 'add': 'Kathmandu'}
#     print(a)


# a = {}
# n = int(input("Enter a number"))
# for i in range(1, n+1):
#     name = input("Enter your name")
#     age = int(input("Enter your age"))
#     add = input("Enter your address")
#     d = {'name': name, 'age': age, 'add': add}
#     a[i] = d
# print(a)

# add element
# a[3] = {'name': 'Ankit', 'age': 45, 'add': KAthmandu}

# delete
# del a[-1]

# WAP to create  result management system for a class
# physics - th,pr
# chemistry -th pr
# math
# english
# Nepali
# grade
# total
d = {}
n = int(input("Enter a number = "))
for i in range(1, n+1):
    name = input("Enter your name = ")
    pt = int(input("Enter your marks of Physics Theory = "))
    p = int(input("Enter your marks of Physics Practical ="))
    ct = int(input("Enter your marks of Chemistry Theory = "))
    c = int(input("Enter your marks of Chemistry Practical ="))
    m = int(input("Enter your marks of Maths = "))
    e = int(input("Enter your marks of English = "))
    n = int(input("Enter your marks of Nepali = "))
    tot = p+c+m+e+n
    l = {'Name': name, 'Physics': [pt, p], 'Chemistry': [ct, c],
         'Maths': m, 'English': e, 'Nepali': n, 'Total': tot}
    d[i] = l
    per = tot/5

    if (per >= 80):
        grade = "Distinction"
    elif (per >= 70 and per < 80):
        print("First Division")
    elif (per >= 60 and per < 70):
        print("Second Division")
    elif (per >= 50 and per < 60):
        print("Third Division")
    else:
        print("Failed")
print(d)
