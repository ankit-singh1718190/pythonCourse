# # class MyClass():
# #     def __init__(self) -> None:
# #         pass
# # class myclas1(MyClass):
# #     def __init__(self) -> None:
# #         super().__init__()    
# class Father():#Parient classs
#     def land(self):
#         print("i have some land")
# class Son(Father):#Child Class
#     def mony(self):
#         print("having some money")
# class SoneOther(Son):
#     def Son2(self):
#         print("i am second son")        
# obj=SoneOther()
# obj.land()
# obj.mony()  
# obj.Son2()    

class A():
    # num1=2
    # num2=3
    num1=int(input("Enter the number"))
    num2=int(input("Enter the number"))
    def add(self):
        print(self.num1+self.num2)
class B(A):
    def multi(self):
        print(self.num1*self.num2)
obj=B()
obj.add()
obj.multi()