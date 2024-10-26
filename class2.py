#methods And Constractor
# a constractor is also a types of method it will automatically
# call when you create a class object
class Myclass():
    a=10
    def mymethdo(self):
        self.c=self.a*self.a
        print(self.c)
    def Mymethod1(self,a,b):
        print(a+b)    


obj=Myclass()
obj.mymethdo()  
obj.Mymethod1(2,3)      