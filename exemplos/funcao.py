from datetime import datetime

def menu_calculadora():
    print("menu calculadora")
    print("1 - adição")
    print("2 - subtração  ")
    print("3 - multiplicação ")
    print("4 - divisão")

#menu_calculadora()

def ola_nome(nome):
    print("Ola ", nome)
    # ola_nome("Fran")

def calcula_idade(ano_nascismento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascismento
    return idade

def exibir_idade(idade):
    print("a sua idade é", calcula_idade(1997))

#menu_calculadora()

def ola_nome(nome):

    ola_nome("Fran")



def solicita_ano_nascimento():
    while True:
        try:
            ano_nascismento = int(input("Digite o ano de nascimento: "))
            if ano_nascismento > datetime.now().year:
                print("digite um ano de nascimento")
            else:
                print("digite um ano menor que o atual ")
        except ValueError:
            print("digite somente numeros. ex: 1997 ")

print(calcula_idade(1997))

#exibir_idade(calcula_idade(ano_nascimento)
#ola_nome("Fran")