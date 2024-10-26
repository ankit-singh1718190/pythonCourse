#Decorater
#Funcation which takes other 
# Functions as input, add additional Functionalties and return it
def DecorFuncatin(func):
    def inner():
        func()#Execting Funcation
        print("Ankit Singh")##Add new
    return inner    

def myFuncation():
    print("Ankit singh")

a=DecorFuncatin(myFuncation) 
a()
