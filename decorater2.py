#Decorater
#https://youtu.be/PGzbKNkWoCs?si=C9iTSGCzEmFPlngj
def decoraterFun(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        func(a,b)    
    return inner      
def myFun(a,b):
    print(a/b)
a=decoraterFun(myFun)  
a(10,5)
