# def take_value():
#     p=int(input("Enter principle: "))
#     t = int(input("Enter time : "))
#     r = int(input("Enter rate : "))
#     return [p,t,r]
#
# def calculate():
#     # p,t,r =take_value()
#     # return p*t*r/100
#     res=take_value()
#     p=res[0]
#     t=res[1]
#     r=res[2]
#     return p*t*r/100
#
# def display():
#     print("The interest is: ",calculate())
#
# display()


# name=input("Enter name: ")
# time=int(input("Enter time: "))
# def repeat(data,ntimes):
#     increment=1
#     while increment<=ntimes:
#         print(data)
#         increment+=1
#
# repeat(name,time)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def num(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return [add,sub,mul,div]

result= num(a,b)
print (f"Addition:{result[0]}, subtraction: {result[1]}, multiplication: {result[2]}, division: {result[3]} ")