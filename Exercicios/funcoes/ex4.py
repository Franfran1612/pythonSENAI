#Classificador de triangulo: Crie uma função que receba três números como parâmetros que serão os
# lados de um triângulo e retorne se ele é equilátero, isósceles ou escaleno.
#Equilátero se todos os lados possuem a mesma medida.
#Isósceles se dois lados possuem a mesma medida.
#Escaleno se todos os lados possuem medidas diferentes.



def lado1():
    lado1 = int(input("Digite o lado 1: "))
    return lado1
def lado2():
    lado2 = int(input("Digite o lado 2: "))
    return lado2
def lado3():
    lado3 = int(input("Digite o lado 3: "))
    return lado3

def valor_triangunlo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        return "equilatero"
    elif lado1 != lado3 and lado2 != lado3 and lado1 != lado3:
        return "escaleno"
    else:
        return "isosceles"
lado1()
lado2()
lado3()
resultado = valor_triangunlo(lado1, lado2, lado3)
print(resultado)


