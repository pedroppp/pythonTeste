# coding: utf-8
# teste de funções

def funcao_inicial():
    print("teste funcao")

def soma(x,y):
    total = x + y
    print(" valor total ",total)
    print(" valor total 2 %d" %total)

# parametros default

def login(usuario="teste",senha="123"):
    print(" usuario: %s e senha: %s" %(usuario,senha))


def login2(sistema,usuario="teste",senha="123"):
    print(" usuario: %s e senha: %s do sistema %s" %(usuario,senha,sistema))

def dados_pessoais(nome,sobrenome,idade,sexo):
    print(" nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}\n"
          .format(nome,sobrenome,idade,sexo))

def soma3():
    return 10

def funcRetValMult():
    return 1, 2

def potenciaN(x):
    quadrado = x**2
    cubo = x**3
    return quadrado, cubo

funcao_inicial()
soma(2, 3)
login()
login("root","12345")
login2("Sistemateste")
dados_pessoais("Pedro","Pires","50","MASCULINO")
#ARGUMENTOS NOMEADOS
dados_pessoais("Pedro",sexo="MASCULINO",idade="53",sobrenome="Pires")
print(" resultado da soma3 %d" %soma3())

# retorno de valores multiplos
x, y = funcRetValMult()
print(" Valor retornado de x %d\n Valor retornado de y %d" %(x,y))

a,b = potenciaN(10)
print(" Quadrado %d "%a)
print(" Cubo %d "%b)
