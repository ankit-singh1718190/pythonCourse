# class Student():
#     def __init__(self,fullname): #Constractor
#         self.name=fullname
#         #self=fullname
#         print("Adding new student")
   
# s1=Student("ankit")
# print(s1.name) 
# s2=Student("pooja")
# print(s2.name) 
############
# constractor __init__   
# class car():
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clh=False
class Account():
    def __init__(self,blance,accountNumber):#Constractor
        self.blance=blance
        self.accountNumber=accountNumber

obj=Account(10000,133332)
print(obj.blance)
print(obj.accountNumber)
