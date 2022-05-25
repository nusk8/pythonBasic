#Inheritance

class Laptop:

    def __init__(self,company_name):
        self.company_name=company_name

    def brand(self,brand):
        return f'Brand{brand}'

    def model(self,model):
        return f'Model{model}'

    def price(self,price):
        return f'Price {price}'

class Demo:
    def __init__(self,company_name,location):
        print("test")

class Dell(Demo,Laptop):
    def __init__(self,company_name,logo):
        # Laptop.__init__(self,company_name)
        # super().__init__(company_name)
        Demo.__init__(self,company_name,logo)
        Laptop.__init__(self, company_name)
        print(logo)




    def memory(self,memory):
        return f'Memory {memory}'



obj=Laptop('dell',)
print(obj.brand('Dell'))
