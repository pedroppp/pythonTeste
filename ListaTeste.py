lista = [100,200,300,400]
for item in lista:
    item += 1000
    print(item)
print(lista)
# agora serão acrescidos valore a lista
print(50*'-')
print(' acrescimo de valores a lista ')
print(50*'-')
print(50*'-')
lista1 = [10,20,30,40]
print(lista1)
#lista_indice = [0,1,2,3]
# lista_indice = range(0,4) # inicia 0 com 4 elementos
lista_indice = range(4)
for indice in lista_indice:
    lista1[indice] += 1
print(lista1)
# opcao mais eleganta
print(50*'-')
for indice in range(4):
    lista1[indice] += 1
print(lista1)
print(50*'-')
print(50*'- forma automatica')
print(50*'-')
for indice in range(len(lista1)):
    lista1[indice] += 1
print(lista1)
