# # class  MyClass:
# #     a=9
# #     def MyMethod(self):
# #         print(self.a)
# # demobject=MyClass()
# # demobject.MyMethod()    
# class student():
#     def MyMethod(self):
#         self.Roll=int(input("Enter the roll"))
#         self.Name=input("Enter the Name")
#     def MySecMetod(self):
#         print(self.Roll)
#         print(self.Name)    
# a=student()
# a.MyMethod()
# a.MySecMetod()

#############
class student():
    def __init__(self,name,roll):
        self.n=name
        self.r=roll
    def MySecMetod(self):
        print(self.n)
        print(self.r)    
a=student("ankit",333)
a.MySecMetod()