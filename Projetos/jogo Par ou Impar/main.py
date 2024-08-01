import random #sorteio um numero
numero_aleatorio = random.randint(1, 100)
print("play")
par = "P"
impar = "I"
while True:
        tipo = str(input('Você quer Par ou Impar? [P/I]: '))
        jogador = int(input("Digite um número: "))
        if tipo == "P":
            