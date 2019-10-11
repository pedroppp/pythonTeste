
lista = ['aaa','bbb','ccc','ddd']
print(lista)
lista.append('eee')
print(lista)
lista.insert(0,'000')
print(lista)
lista[0] = '000a'
print(lista)
lista.clear()
print(lista)
lista = ['aaa','bbb','ccc','ddd']
lista.pop() # remove ultimo elemento
print(lista)
lista.pop(0)
print(lista)
lista.pop(-1)
print(lista)
lista = ['aaa','bbb','ccc','ddd','eee']
print(lista)
del(lista[2:4])
print(lista)
lista = ['aaa','bbb','ccc','ddd','eee','fff']
del(lista[::2])
print(lista)

