def cacular_resistencia():
    tensao = float(input("digite o valor de tensao: "))
    corrente = float(input("digite o valor de corrente: "))
    return tensao / corrente

def calcular_tensao():
    corrente = float(input("digite o valor de corrente: "))
    resistencia = float(input("digite o valor de resistencia: "))
    return corrente * resistencia

def calcular_corrente():
    tensao = float(input("digite o valor de tensao: "))
    resistencia = float(input("digite o valor de resistencia: "))
    return tensao / resistencia

def calcular_resistor():
    tensao_fonte = float(input("digite o valor de tensao_fonte: "))
    tensao_dispositivo = float(input("digite o valor de tensa_dispositivo: "))
    corrente_dispositivo = float(input("digite o valor de corrente_fonte: "))
    return (tensao_fonte - tensao_dispositivo) * corrente_dispositivo

print("calculadora de 0hm")
print("*****************************************************************************")
print("MENU: ")
print("0 - sair")
print("1 - resistencia")
print("2 - tensão")
print("3 - corrente")
print("4 - resistencia necessaria para um resistor ")
print("******************************************************************************")

while True:
    try:
        calculo = input("qual opcao deseja calcular: ")

        if calculo == "1":
            resistencia = cacular_resistencia()
            print(f"A resistencia de {resistencia} ")
        elif calculo == "2":
            tensoa = calcular_tensao()
            print(f"A tensao é {tensao}")
        elif calculo == "3":
            corrente = calcular_corrente()
            print(f" A corrente de {corrente} ")
        elif calculo == "4":
            resistor = calcular_resistor()
            print(f"O resistor deve ser o de {resistor} 0hm")
            break
    except ValueError:
        print("Por favor, digite apenas numeros")

