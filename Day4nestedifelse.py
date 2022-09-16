# Simple calculator
# a = int(input("Enter the value of a ="))
# b = int(input("Enter the value of b = "))
# o = input("Enter the operator + / * - ")
# if o == '+':
#     c = a+b
#     print(c)
# elif o == '-':
#     c = a-b
#     print(c)
# elif o == '/'and o !=0:
#     c = a/b
#     print(c)
# elif o == '/'and o !=0:
#     print("The value cannot be divided")
# elif o == '*':
#     c = a * b
#     print(c)
# else:
#     print("invalid operator")

# Nested if/else
# Syntax:
# if <conditon>:
#     if<condition>:
#         <operation>
#     elif <condition>:
#         <operation>
#     else:
#         <operation>
# else:
#     <operation>
# Example of Nested IF/ ELSE
x = int(input("Enter an value of x =  "))
if x > 0:
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("wrong input")
