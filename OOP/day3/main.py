#Incapsulation

# class College:
#     def __init__(self,name,location):
#         self._name=name
#         self.__location=location
#
#
# class Students(College):
#     def into(self):
#         print(self._name)
#         print(self.__location)
#
#     ##public, private, protected: java,php,c#
#     # def __init__(self,name,age):
#     #     self._name=name
#     #     self.age=age
#
#     def __getName(self):
#         return self.__name
#
#
# obj=Students("Ram",20)
# obj.info()
#
# # print(obj._getName())


# class College:
#     __name=''
#
# obj=College()
# obj.__name='Ram' #this __name is not the same as __name in line 30
# print (obj.__name)



# class College:
#     __name='' #private property declared here
#
#     def set_name(self,name):
#         self.__name=name
#
#     def get_name(self):
#         return self.__name
#
#     # def __delete__(self):
#     #     del self.__name
#
# obj=College()
# obj.set_name('Ram')
# print(obj.get_name())
#
# # del obj
# # print(obj.get_name())


# class Employee:
#
#     def __init__(self): #constructor should run first but new runs faster
#         print("I am Employee")
#
#     def __str__(self):
#         print( 'Employee')
#
#     def __call__(self,*args, **kwargs):
#         print("I am employee call method")
#
#     def __new__(cls,*args,**kwargs):
#         print("I am employee new method")
#         return object.__new__(cls)
#
#     def __repr__(self):
#         pass
#
#     # def __init__(self):
#     #     print("I am in init")
#     #
# #     def __del__(self): #__del__ is destructor which runs at the last
# #         print("I am in del")
# #
# obj=Employee()
# obj()
# # print(obj)



# #Proper decorator example
#
# class Employee:
#     enm_name=''
#
#     @property
#     def test(self):
#         return f"My name is {self.enm_name}"
#
#     @test.setter
#     def test(self,name):
#         self.enm_name=name
#
# obj= Employee()
# obj.test='sophia'
# print(obj.test)


# class Employee:
    # def __init__(self,name,age):
    #     print(name)
    #     print(age)

#     @staticmethod
#     def emp_name():
#         return "Sophia"
#
#     @staticmethod
#     def add(x,y):
#         return x+y
#
# Employee.emp_name()
# print(Employee.add(20,30))


# class Employee:
#     enm_name=''
#
#     @property
#     def test(self):
#         return f"My name is {self.enm_name}"
#
#     @test.setter
#     def test(self,name):
#         self.enm_name=name
#
#
#     @test.deleter
#     def test(self):
#         del self.enm_name
#
# obj= Employee()
# obj.test='sophia'
# print(obj.test)
# del obj.test
# print(obj.test)


# #things to learn yourself
# class Test:
#     a=10
#
#     @classmethod
#     def get(cls):
#         cls.a
#
#     def __repr__(self):
#         pass
#     def __add__(self, other):
#         padd
#
# class User(object):
#     pass
#
# import datetime
# print(datetime.datetime.now())