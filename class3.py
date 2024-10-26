class MyClass():
    def MyMethod(self):
        self.a=23
        self.b=30
        self.c=self.a+self.b
        print(self.c)
obj=MyClass()
obj.MyMethod() 

class Student():
    def MyD(self,a,b):
        print(a*b)
obj=Student()
obj.MyD(2,3)        