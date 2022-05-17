#types of iteration: Definite and indefinite iteration

#While loop: indefinite iteration
#example:
# x=1
# while x<10:
#     print(x, end=' , ')
#     x+=1

# name=input("Enter the name: ")
# num= int(input("Enter the number of times repeated: "))
# increment=1
# while increment<=num:
#     print(f"{name}")
#     increment+=1

#WAP to enter number of times and print total even and odd number

# even=0
# odd=0
# increment=1
# num=int(input("Enter a number: "))
# while increment <=num:
#     if increment%2==0:
#         even+=increment
#     else:
#         odd+=increment
#
#     increment+=1
#
# print(f"Total even: {even}")
# print(f"Total odd: {odd}")

#for loop : definite
#example:

# data=["ram",'sita','gita','hari']
# x=0
# while x<len(data):
#     print(data[x])
#     x+=1

# data=["ram",'sita','gita','hari']
# print(dir(data))

# data=["ram",'sita','gita','hari']
# for name in data:
    # print( name)

# data=["ram",'sita','gita','hari']
# a=iter(data)
# print(a.__next__())
# print(dir(data))

# data=[
#     ["ram",'sita','gita','hari'],
#     ["laxmi",'sophia','gopal'],
# ]
# for nams in data:
#     for name in nams:
#         print(name)

# print(range(10))
# for x in range(10):
#     print (x)

#Iterables


#WAP to enter number of students enter
#five subject marks and print total marks and average marks of each student division wise

num=int(input("Enter the number of students: "))
increment=1
while increment<=num:

    nep=float(input("Enter the marks of Nepali: "))
    eng=float(input("Enter the marks of English: "))
    math=float(input("Enter the marks of Math: "))
    sci=float(input("Enter the marks of Science: "))
    pop=float(input("Enter the marks of Population: "))
    total= nep+eng+math+sci+pop
    avg= total/5
    print(f"The total marks is:{total}")
    print(f"The avrage marks is: ")
    if avg>=75 and avg<=100:
        print("Distinction")
    elif avg>=60 and avg<75:
        print("First division")
    elif avg>=45 and avg<60:
        print("Second division")
    elif avg>=35 and avg<45:
        print("Third division")
    else:
        print("fail")