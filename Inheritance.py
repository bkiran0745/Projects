c = 10
d = 10
#   ======================= SingleLevel Ingeritance =============================
class Airth():
    def add(self,a,b):
        print("+ :",a+b)

class Airth1(Airth): # Inheriting the class Airth in Airth1
    def sub(self,a,b):
        print("- :",a-b)

o = Airth1()
o.add(c,d)
o.sub(c,d)


class default():
    print("This is Executed by Default Constuctor...!!") # This executes directly bcoz fo it is not written in any method as it  acts as a default constructor and executes this line
    def b(self):
        print("Hello from B")
class A(default):
    print("This is class A")

o = A()
o.b()




# ------------------------- MultiLevel Inheritance --------------------
class one():
    print("a")
    def one(self):
        print("Class One")
class Two(one):
    print('B')
    def Two(self):
        print("Class Two")
class Three(Two):
    print("c")
    def Three(self):
        print("Class Three")
class four(Three):
    print("D")
    def Four(self):
        print("Class Four")

abj = four()
abj.one()
abj.Two()
abj.Three()
abj.Four()


# ============================= Multiple Inheritance ==============================

class a():
    print("This is Multiple Inheritance")
    def a(self):
        print("A")
class b():
    def b(self):
        print("B")
class c():
    def c(self):
        print("C")
class d(a,b,c):
    def d(self):
        print("D")

ob = d()
ob.a()
ob.b()
ob.c()


# ================= Hybrid Inheritance ======================

