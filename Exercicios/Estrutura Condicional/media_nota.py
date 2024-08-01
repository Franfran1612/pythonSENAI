#Solicite duas notas de um aluno e
# calcule a média.
# Se a média for maior ou igual a 70,o aluno está aprovado.
# Caso contrário, está reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

if media >70:
    print("aprovado")

else:
    print("reprovado")
