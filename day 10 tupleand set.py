# Set
# ->no indexing
# -> no duplicate data
# -> unordered
# -> mutable

# a = set()
# b = {1, 2, 3, 4, 2, 13}
# c = {'Ball', 'Apple', 'Cat'}
# print(b)
# print(c)
# print(type(b))
# print(type(c))
# for i in c:
#     print(i)
# c.add('Dog')
# print(c)

# l = set()
# n = int(input("Enter a number"))
# for i in range(n):
#     x = int(input("ENter number"))
#     l.add(x)
# print(l)

# a = {1, 23, 4, 3, 45, 6, 47}
# b = {1, 5, 6, 2, 1, 0}
# a.update(b)
# print(a)

# a.remove(3)

# main function of a set are
# union
# intersection
# difference
u = {'Shyam', 'Jack', 'Sarita', 'Hari',
     'Nabin', 'Ram', 'Sabin', 'Bikesh', 'Nikesh'}
a = {"Ram", "Shyam", "Hari", "Nabin", "Sabin"}
b = {"Hari", "Nabin", "Jack", "Sarita"}
# c = a.union(b)
# d = a.intersection(b)
# e = a-b
# f = b.difference(a)
# print(c)
# print(d)
# print(e)
# print(f)
c = a.issubset(u)
print(c)
