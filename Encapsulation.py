#Procated the variable or Method
#_ Single Underscor using for Protected
# __ DubalUnderscoree using For Private
class MyClass():
    _a=10#Protected
    __b=20 #Private
    def MyDemo(self):
        print(self._a)
        print(self.__b)
obje=MyClass()
obje.MyDemo()        