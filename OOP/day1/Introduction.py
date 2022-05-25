# ##declare a class
# class Introduction:
#     ##body part of the class
#     x=10 # x and 10 is attribute or property
#
#     def test(self): #method
#         pass #does not return anything
#
# ##declaring an object: instance of the class
# obj=Introduction()
# ##access the object by using dot(.)
# print(obj.x)
# print(obj.test())


# class Students:
#     def name(self,name):
#         print(f'Student name is {name}')
#
#     def age(self,age):
#         print(f'Student age is {age}')
#
# obj=Students()
# obj.name('John')
# obj.age(20)
# obj.name('sita')
# obj.age(30)
#
# print (obj.name)
# print(obj.age)

class User:
    name='Sophia'

    def get_name(self): #self is object of the class User
        print (self.name)
        print(self.age())
    def age(self):
        return 10

obj=User()
obj.get_name()


class Introduction:
    total=0

    def __init__(self,name,age):
        self.user_name=name
        self.usr_age=age
        Introduction.total+=1


obj=Introduction('John',20)
obj1=Introduction('Sita',30)
obj2=Introduction('Hari',40)
obj3=Introduction('Geeta',50)


print(obj.total)

#construction cannot declare define type

#property decorator
#inheritance
