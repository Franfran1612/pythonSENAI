import random #sorteio um numero
numero_aleatorio = random.randint(1, 100)
print("play")

#instrução
print("adivinhe o numero:")
print("")
print("maior que o numero 0")
print("menor que o numero 100")
sim = 1
nao = 2
while True: #while é para repitir
    numero_jogador = int(input("Digite um numero: "))  # input entrada de informação
    if numero_jogador == numero_aleatorio:
        print("parabens, voce acertou")

        continuarOuNao = int(input("deseja continuar? 1=sim, 2=nao "))
        if continuarOuNao == 1:
            sim
        else:
            nao
            break
    elif numero_jogador > numero_aleatorio:
        print("o numero que voce colocou é maior que o numero sorteado ")
    else:
        print("ele é menor que o numero que foi sorteado ")
