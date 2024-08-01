# Calculadora Básica: Crie uma função que receba dois números como parâmetros
# e exiba o resultado das operações básicas de adição, subtração, multiplicação e divisão.


def soma_adicao( numero1,numero2 ):
    resultado_final = numero1 + numero2
    return resultado_final

def soma_subtracao(numero1,numero2):
    resultado_final = numero1 - numero2
    return resultado_final

def soma_multiplicacao(numero1,numero2):
    resultado_final = numero1 * numero2
    return resultado_final

def soma_divisao(numero1,numero2):
    resultado_final = numero1 / numero2
    return resultado_final


adicao = 1
subtracao = 2
multiplicacao = 3
divicao = 4

print("1 adicao")
print("2 subtracao")
print("3 multiplicacao")
print("4 divicao")

escolha = int(input("digite um numero: "))

if escolha == adicao:
    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
    print("o resultado final é ", soma_adicao(numero1,numero2),)

elif escolha == subtracao:
    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
    print("o resultado final é ", soma_subtracao(numero1,numero2),)

elif escolha == multiplicacao:
    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
    print("o resultado final é ", soma_multiplicacao(numero1,numero2),)

else:
    numero1 = int(input("digite  o primeiro numero: "))
    numero2 = int(input("digite o o segundo numero: "))
    print("o resultado final é ",soma_divisao(numero1,numero2),)
