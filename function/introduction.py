# type of functions
# 1. Inbuilt function: built in function
# 2. User defined function: user defined function

# Inbuilt function example:
# 1. abs()
# 2. pow()
# 3. max()
# 4. min()
# 5. round()

# print(dir(__builtins__))

# User defined functions examples:

# #define function
# def function():
#     #function body
#     print("Hello")
#
# #call function
# function()
# function()

# parameters and arguments
# parameters examples:

# def users(name,age,address):
#     print("Hello",name)
#     print("You are",age,"years old")
#     print("You live in",address)

# users('Kiti',23,"New York")


# def add(x, y):
#     print(x + y)
# #ctrl+alt+l for spacing
#
# add(40, 50)
# add(89, 60)

#Optional parameters example:

# def add(x,y=0): #y is optional
#     print(x+y)
#
# add(40,30)

#* is array which is a collection (arg,kwargs)
#*args examples:

# def users(*names):
#     print(names)
#
# users('Ram','Shyam','Hari','anu')


#** Keywords examples:

# def users(*names,**data):
#     print(names)
#     print(data)
#
# users('Ram','Shyam','Hari',name='John',age=30,address='New York')

# def test():
#     print("Hello World")
#
# def get():
#     test()
#
# get()

#Return types function examples:

# def add(x, y):
#     return x + y
#
# print(add(20,40))

# def users():
#     pass
#
# print(users())

# def add_sub(x,y):
#     tot=x+y
#     sub=x-y
#     return [tot, sub]
#
# print(add_sub(40,50))

# x = 10
#
# def test():
#     global x
#     x=x+39
#     print(x)
#
# test()
# print(x)


#Inline functions example: anonymous functions

# a=lambda x,y:x+y
# print(a(20,30 ))
#
# def a(x,y):
#     return x+y
# print(a(20,30))


#Recursion function:

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(5))

#5-1:4=20
#4-1:3=60
#3-1:2=120


#nested function

# def users():
#     def name(new_name):
#         return f"I am {new_name}"
#
#     return name
#
# print(users()('Ram'))

# a=users()
# print(a())

#Function generator

# def users():
#     yield 'ram'
#     yield 'Shyam'
#     yield 'Hari'
#
# a=users()
# # for i in a:
# #     print(i)
#
# print (a.__next__())
# #double underscore method is dondon method
# print (a.__next__())
# print (a.__next__())

# print(type(users()))


# def connection():
#     """
#     This is a connection function used to connect to the database
#     """
#     return True
# print(connection.__doc__)


