print("Calculadora de Ohm")

print("calcule o resultado da operação ")
print("1 - tensão\n2 - corrente\n3 - resistencia\n4 - resistencia resistor")
tensao = 1
corrente = 2
resistencia = 3
resistencia_resistor = 4

mensagem = int(input("digite um numero: "))

if mensagem == tensao:
    resistencia = float(input("qual é a resistencia eletrica em Ω "))
    corrente = float(input("qual é a corrente eletrica em A "))
    resultado_final = resistencia * corrente
    print("o resultado final é ", resultado_final, "V")

elif mensagem == corrente:
    tensao = float(input("qual é a tensão em V "))
    resistencia = float(input("qual a resistencia eletrica em Ω "))
    resultado_final = tensao / resistencia
    print("o resultado final é ", resultado_final, "A")

elif mensagem == resistencia:
    tensao = float(input("qual é a tensão em V "))
    corrente = float(input("qual a corrente eletrica em A "))
    resultado_final = tensao / corrente
    print("o resultado final é ", resultado_final, "Ω")

elif mensagem == resistencia_resistor:
    tensao_de_fonte = float(input("qual é a tensao da fonte em V "))
    tensao_do_led = float(input("qual é a tensao do led em V "))
    corrente_de_led = float(input("qual é a corrente de led em A "))
    resultado_final = (tensao_de_fonte - tensao_do_led) / corrente_de_led
    print("o resultado final é ", resultado_final, "Ω")

else:
    print("imposilvel fazer calculo")
