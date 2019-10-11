lista = [1,2,3,4,5,6,7,8,9,0]
print(lista)
print(type(lista))
lista1 = list("testo teste")
print(lista1)
a = (5)
print(type(a))
b=(5,)
print(b)
print(type(b))
lista2 = [['a','b','c'],[5,6,7],[2]]
print(len(lista2))
# "-1" é o último elemento da lista
print("ultimo elemento da lista ",lista2[-1])
#contatenacao de listas
lista = lista + lista2
print(lista)
lista.append(lista1)
print(lista)
del(lista[-1])
print(lista)
listateste = 10*['a']
print(listateste)
listateste += 5*['b']
print(listateste)
print(50*'-')
