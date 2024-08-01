print("calculadora de ohm")
print("")

print("digite 1 para calcular a resistencia")
print("digite 2 para calcular a tensão ")
print("digite 3 para calcular a corrente em circuito")
print("digite 4 para calcular a resistensia resistor")

print("")

resistencia = 1
tensao = 2
corrente = 3
resistencia_re = 4
sair = 0

opcao = int(input("digite o número da escolha desejada:"))

while opcao != 0:

    if opcao == 1:
        while True:
            try:
                tensao1 = float(input("digite a tensão desejada:"))
                if tensao1 > 0:
                    break
            except ValueError:
                print("valor invalido. digite um numero utilizando o ponto para separa. ex:1.0")
        while True:
            corrente = float(input("digite a corrente eletrica (I) ou (A):"))
            if corrente > 0:
                break
            conta = tensao / corrente
            print(f"A resistencia é {conta} ohms ")
    elif opcao == 2:
        while True:
            try:
                resistencia = float(input("digite a resistencia eletrica (R):"))
                if resistencia > 0:
                    break
            except ValueError:
                print("valor invalido. digite um numero utilizando o ponto para separa. ex:1.0")

        while True:
            corrente2 = float(input("digite a corrente eletrica (I) ou (A):"))
            if corrente2 > 0:
                break
            conta2 = resistencia * corrente2
            print(f"A tensão elétrica é {conta2} volts (V) ")

    elif opcao == 3:
        while True:
            try:
                tensao2 = float(input("digite a tensão elétrica (V):"))
                if tensao2 > 0:
                    break
            except ValueError:
                print("valor invalido. digite um numero utilizando o ponto para separa. ex:1.0")
        while True:
            resistencia3 = float(input("digite a corrente eletrica (R):"))
            if resistencia3 > 0:
                break
            conta3 = tensao2 / resistencia3
            print(f"a corrente eletrica é {conta3} ampares")

    elif opcao == 4:
        while True:
            try:
                tensao4 = float(input("digite a tensão da fonte"))
                if tensao4 > 0:
                    break
            except ValueError:
                print("valor invalido. digite um numero utilizando o ponto para separa. ex:1.0")

                tensao5 = float(input("digite uma tensão da fonte: "))
                if tensao5 > 0:
                    break
            except  ValueError:
                print("valor invalido. digite um numero utilizando o ponto para separa. ex:1.0")
        while True:
            corrente = float(input("digite a corrente de LED:"))
            if corrente > 0:
                break

        ta4 = tensao4 - tensao5
        conta5 = conta4 / corrente
        print(f"A resistencia necessaria para o resistor é {conta5} ohms ")
    else:
        print("opcao invalida")
        print("")

        print("digite 1 para calcular a resistencia")
        print("digite 2 para calcular a tensão ")
        print("digite 3 para calcular a corrente em circuito")
        print("digite 4 para calcular a resistensia resistor")

        opcao = float(input("escolha uma opcao:"))




