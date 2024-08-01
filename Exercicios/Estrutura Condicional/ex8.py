#faixa = 56.072,01_238.532,00_7,50%
#faixa = 238.532,01_522.400,00_15%
#faixa = 522.400,01_987.600,00 _22,50%
#faixa = 987,600  27,50%
while True:
     #comando de execução
    try:
        renda = float(input("digite sua renda anual bruta para descontar  para calcular seu desconto do posto de renda: "))
        break
        #except mostrar quando erra
    except ValueError:
        print("dado invalido"
              ",")

if renda < 56072.00:
    print("desconto 0%")
elif renda >= 56072.01 and renda <= 238532.00:
    desconto = (7.50 / 100) * renda
    print(f"O seu desconto é de R$ {desconto} ")
elif renda >= 238532.01 and renda <= 522400.00:
    desconto = (15 / 100) * renda
    print(f"o seu desconto é de R$ {desconto} ")
elif renda >= 522400.01 and renda <= 987600.00:
    desconto = (22.50 / 100) * renda
    print(f"O seu desconto é de R$ {desconto}" )
elif renda >= 987.600:
    desconto = (27.50 / 100) * renda
    print(f"O seu desconto é de R$ {desconto} ")


#def exibir_idade(idade):

 #print("a sua idade é", idade, "anos")