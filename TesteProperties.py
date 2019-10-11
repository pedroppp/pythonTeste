
class A:
    def __init__(self):
        self._var = 0;
    def get_var(self):
        print(" O valor esta sendo lido ")
        return self._var
    def set_var(self,x):
        print("O valor esta sendo atribuido ")
        self._var = x
    var = property(fget=get_var,fset=set_var)

a = A()
a.var = 10
print(a.var)
