#Same Object having Defferent behavior
#OverLoading 
# class MyClass():
#     def MyDef(self):
#         print("Welcome")

#     def MyDef(self,FristName=''):
#         print(FristName)   

#     def MyDef(self,FristName='',LastName=''):
#         print(FristName,LastName) 

# obj=MyClass()
# obj.MyDef('ankit','singh') 
################
class MyClass():
    def MyDef(self,FristName='',LastName=''):
        print("WelcomE",FristName,LastName) 

obj=MyClass()
obj.MyDef()
obj.MyDef('ankit','singh')
#overiding

class A():#prant Class
    def fun(self):
        print("i am in Class A")
class B(A):#child Class
    def fun(self):
        print("i am in class B")
obj=B()
obj.fun()