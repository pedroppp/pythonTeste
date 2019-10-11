td = {}
print(type(td))
d1 = dict()
print(type(d1))
d1['aaa'] = 1000
d1['bbb'] = 2000
d1['ccc'] = 3000
print(d1)
d2= dict()
d2 = {1.1:"teste1",2.2:"teste2",3:"teste3"}
print(d2)
print(50*'-')
print(50*'-')
print(d2[1.1])
tel = {}
tel = {
    1111111 : "Jose da Silva",
    2222222 : "Ana Maria",
    3333333 : "Antonio da Sival",
    4444444 : "Joao da Silva",
    5555555 : "Paulo da Silva",
    6666666 : "Marcos de Oliveira"
}
print(tel)
print(len(tel))
del(tel[1111111])
print(tel)
print(tel.keys())
print(tel.values())
print(tel.get(2222222))
print(tel)
print(tel.popitem())
print(tel)