#variables.py
#This file contains programs related to variables

name = "Shruti"
age = 20
branch = "CSE AI-ML"

print(name, age, branch) 

#we can stores two variables at a time
x, y = 10, 20
print(x,y)

# type() prints the type of variables
print(type(x))
print(type(name))

# Swap two number using a temporary variable
a = 20
b = 50

temp = a
a = b
b = temp
print(a,b)

# Swap two numbers without using a third variable by using python's built-in swapping
a, b = b, a