#Solicite ao usuário um número de 1 a 12(representando um mês do ano)
# exiba o nome correspondente ao mês (por exemplo, 1 para "Janeiro", 2 para "Fevereiro", etc.)

ano = int(input("Digite o numero: "))
mes = "hoje é"

if ano == 1:
    print(mes, "janeiro")
elif ano == 2:
    print(mes, "fevereiro")
elif ano == 3:
    print(mes, "março")
elif ano == 4:
    print(mes, "abril")
elif ano == 5:
    print(mes, "maio")
elif ano == 6:
    print(mes, "junho")
elif ano == 7:
    print(mes, "julho")
elif ano == 8:
    print(mes, "agosto")
elif ano == 9:
    print(mes, "setembro")
elif ano == 10:
    print(mes, "outubro")
elif ano == 11:
    print(mes, "novembro")
elif ano == 12:
    print(mes, "dezembro")
else:
    print("valor invalido")
