
class Retangulo:
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h
    
r = Retangulo(5,7)
print("Area do retangulo",r.area())