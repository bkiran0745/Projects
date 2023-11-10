# -------------------------- Method Overloading [ Compile Time Polymorphism ] -----------------------------
# Functions with same name but different parameters are called method overloading.

from multipledispatch import dispatch
class A():
    @dispatch(str,str) # Before using this it raises a Error .
    def a(self,a,b):
        print(a+b)
    @dispatch(str,str,str)
    def a(self,a,b,c):
        print(a+b+c)
o = A()
o.a('kiran ','busari')
o.a('BITM ','Ballari ','583102')
