
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