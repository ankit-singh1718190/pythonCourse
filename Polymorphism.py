# print(5+5)
# print("5"+"5")#same object having defferent behavior
# print(len("ankit"))
# print(len(["ankit","singh"]))
#method Overloading
class Area():
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)    
        else:
            print("not find")    
obj=Area()
obj.find_area()  
obj.find_area(10)
obj.find_area(10,20)     


