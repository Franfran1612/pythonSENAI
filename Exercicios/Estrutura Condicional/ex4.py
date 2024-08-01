while True:
    try:
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite outro numero: "))

        if num1 > num2:
            print("o primeiro numero é maior que o segundo")
        elif num2 > num1:
            print("o segundo numero é maior que o primeiro")
            #else é quando os dois numeros sao iguais
        else:
            print("os dois numeros sao iguais")
        break

    except ValueError:
        print("digite apenas numeros")