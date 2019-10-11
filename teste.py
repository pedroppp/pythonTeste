""""
print(" teste linhas ")
print("primeira linha")
"""
print("segunda linha")
if True:
    print(1+1)
    print("continua no true ")
print("apos if");print("apos ;");
a = 10
a
num_ref = 7.5
texto = "teste de texto"
print(type(texto))
print(type(a))

print(" O valoe da variavel a é :",num_ref)
print(" >> O valor da variaval é %.10f" %num_ref)
print(" >>> O valor da variavel é "+str(num_ref))
print(" Olha o texto >>> %s" %texto)
"""
login = input("login")
se = input("senha")
print(" usuario %s senha %s" %(login,se))
b= 10/6
print(b)
print(" O valor flutuante é %10f" %b)
c=10//6
print(" O valor inteiro é %i" %c)
num1 = float(input("Digite o numerador :"))
num2 = float(input("Digite o denominador :"))
divisao = num1 / num2
resto = num1 % num2
print(" Divisao "+ str(divisao))
print( num1," dividido por ",num2," é igual a ",divisao )
"""
import math
print(dir(math))
print(math.pi)