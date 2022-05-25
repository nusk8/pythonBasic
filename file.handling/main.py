#.txt
#.bin
#.csv
#.json
#.xml
#.yaml

#file mode
#r-read
#a=append
#r+ - read and write
#w+ =write and read
#a+ = append and read


# open('students.txt','w').close()

# handle=open ('students.txt','w')
# print(dir(handle))

# handle=open ('students.txt','a')
# handle.write("test was success\n")
# handle.close()


# obj=open('students.txt','r')
# print(obj.read())

# obj=open('students.txt','r')
# print(obj.readline())

# obj=open('students.txt','r')
# print(obj.readlines())
# obj.close()

# with open('students.txt','r') as obj:
#     print(obj.readlines())

# obj=open('students.txt','r+')
# obj.write('test')
# print(obj.readlines())

# obj=open('students.txt','w+')
# obj.write('test')
# print(obj.readlines())


#example:

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# sum=a+b
#
# handle=open ('students.txt','a')
# handle.write(f"sum: {sum} \n")
# handle.close()


# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# sum=a+b
#
# with open('students.txt','a') as obj:
#     obj.write(f'sum: {sum}\n')


