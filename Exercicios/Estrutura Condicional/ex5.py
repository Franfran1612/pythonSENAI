#Solicite ao usuário um número de 1 a 7(representando um dia da semana)
# exiba o nome correspondente ao dia (por exemplo, 1 para "Domingo", 2 para "Segunda-feira", etc.).

semana = int(input("Digite o numero: "))
data = "hoje é"

if semana == 1:
    print("domingo")
elif semana == 2:
    print("Segunda_feira")
elif semana == 3:
    print("terca_feira")
elif semana == 4:
    print("quarta_feira")
elif semana == 5:
    print("quinta_feira")
elif semana == 6:
    print("sexta_feira")
elif semana == 7:
    print("sabado")
else:
    print("valor invalido")
