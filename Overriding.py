class A():
    def fun(self):
        print("i am in Class A")
class B(A):
    def fun(self):
        print("i am in class B")
obj=B()
obj.fun()            