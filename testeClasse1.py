#coding: utf-8
__author__ = "Pedro Pablo Pinto Pires"


def teste(a):
    print(id(a))

class A:
    def __init__(self):
        print("id do objeto",id(self))

a = A()
print("id do objeto a ",id(a))

teste(a)


