#coding: utf-8

class Retangulo:
    def __init__(self):
        self.h = 0;
        self.b = 0;

    def area(self):
        return self.b * self.h

r1 = Retangulo()
r1.b = 10
r1.h = 5

print("Area do retangulo",r1.area())