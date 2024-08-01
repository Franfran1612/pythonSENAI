# Conversor de Temperatura: Crie uma função que receba um valor de temperatura em graus Celsius como parâmetro
# e retorne o valor convertido para Fahrenheit e Kelvin..

# Criar funcao para solicitar a temperatura em celsius
def solicite_temperatura():
    celsius = int(input("digite um uma temperatura em grau cesius: "))
    return celsius


#Criar uma funcao para calcular e retornar fahrenheit
def retorne_fahrenheit(celsius):
    f = celsius * 1.8 + 32
    return f


#Criar uma funcao para calcular e retornar kelvin
def retorne_kelvin(celsius):
    k = celsius + 273
    return k


celsius = solicite_temperatura()

k = retorne_kelvin(celsius)
f = retorne_fahrenheit(celsius)
print("graus em fahrenheit",f)
print("graus em kelvin",k)





