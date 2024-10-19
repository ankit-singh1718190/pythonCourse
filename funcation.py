# #Funcation
#  #User define Funcation
# #pre DEfine funcation 
# #Simple funcation, funcation with arguments,return types funcation
# def myFucation():
#     a=5 
#     print(a)
# myFucation()    
# def mySumFuncation(a,b):
#     print(a+b)
# c=int(input("Enterd the number1:"))
# d=int(input("Enter the number2:"))


# mySumFuncation(c,d)    

# f=33
# g=33
# mySumFuncation(f,g)
#Return Function
def myReturnFunction(a,b):
    c=a+b
    return c
output=myReturnFunction(12,22)
print(output)

def oddEven(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
out=oddEven(2)    
print(out)
def CheckOddEven(a):
    if a%2==0:
        print("number is Even:")
    else:
        print("Number is odd:")    
CheckOddEven(5)        
