from abc import ABC ,abstractmethod

class A(ABC):
    @abstractmethod
    def foo(self,a,b):
        print(a+b)

class B(A):
    def foo(self,a,b):
        print(a+b)

o = B()
o.foo(100,1000)
o.foo(100,1)