
from asyncore import read
import csv
from operator import concat
import pandas as pd
# Read all the data of csv
# df = pd.read_csv('data.csv')
# print(df)

# Read from the top
# df = pd.read_csv('data.csv', index_col='sn')
# print(df.head(3))

# Read from the bottom
# df = pd.read_csv('data.csv', index_col='sn')
# print(df.tail(3))

# Read in reference of index
# df = pd.read_csv('data.csv', index_col='sn')
# print(df.iloc[0:4])

# Read from the reference of data value
# df = pd.read_csv('data.csv', index_col='name')
# print(df.loc['Shyam':'Gita'])
# read with one condition
# df = pd.read_csv('data.csv', index_col='sn')
# print(df[df['age'] >= 20])

# Read with two conditions
# df = pd.read_csv('data.csv', index_col='sn')
# data = df[(df['age'] >= 30) & (df['add'] == 'Kathmandu')]
# data.to_csv('data1.csv')

# Using dictionary
# data = {'name': ['Ram', 'Shyam', 'Hari'], 'age': [
#     34, 35, 78], 'add': ['Ktm', 'bkt', 'pkr']}
# df = pd.DataFrame(data)
# df.to_csv('clean_data.csv')
# print(df)


# Append in csv
# data = [3, 'kamal', 44, 'Kathmandu']
# with open('clean_data.csv', 'a')as file:
#     x = csv.writer(file)
#     x.writerow(data)
# List inside list appending multiple rows
# data = [['Name', 'Age', 'Address'], ['Ram', 34, 'Ktm'],
#         ['Shyam', 34, 'Ktm'], ['Hari', 34, 'Ktm']]
# with open('clean_data1.csv', 'a')as file:
#     x = csv.writer(file)
#     x.writerows(data)


# Read the csv data into dictionary format
# with open('clean_data1.csv', 'r')as file:
#     reader = csv.DictReader(file)
#     for data in reader:
#         print(data)
#  Read the csv data to list
# add_data = []
# with open('clean_data1.csv', 'r')as file:
#     reader = csv.DictReader(file)
#     for data in reader:
#         add_data.append(data)

#     print(add_data)

data1 = {'Name': 'Ram', 'Age': '34', 'Address': 'Ktm'}, {'Name': 'Shyam',
                                                         'Age': '34', 'Address': 'Ktm'}, {'Name': 'Hari', 'Age': '34', 'Address': 'Ktm'}
data2 = {'Name': 'Ram', 'Age': '34', 'Address': 'tm'}, {'Name': 'hyam',
                                                        'Age': '4', 'Address': 'tm'}, {'Name': 'ari', 'Age': '37', 'Address': 'Bkt'}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df = pd.concat([df1, df2])
print(df)
