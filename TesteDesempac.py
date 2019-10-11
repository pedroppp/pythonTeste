# Empacotamento e desempacotamento

def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

tupla = "Pedro","Pires", 52
pessoa(tupla[0],tupla[1],tupla[2])
pessoa(*tupla)
print(50*"-")
tupla = ["Jose","Silva",44]
pessoa(*tupla)

# Empacotamento e desempacotamento de dicionários
d = {"nome":"Joao", "sobrenome":"Oliveira","idade":35}
print(50*"-")
pessoa(**d)


#desempacotamento de lista

def funcaoT(a,b,c):
    print("Argumento a ",a)
    print("Argumento b ",b)
    print("Argumento c ",c)

print(50*'-')
print(50*'-')
lista= [12,11,10]
lista.sort()
funcaoT(*lista)

#desempacotamento de tupla
# tupla é imutavel
print(50*'-')
print(50*'-')
tupla = 11,10,12
# Desempacotamento dos elementos da tupla em uma lista
l = [*tupla]
l.sort()
funcaoT(*l)

# funcao zip associacao de listas que gera um dicionario
z = zip(("a","b","c"),(1,2,3))
print(z)
print(dict(z))