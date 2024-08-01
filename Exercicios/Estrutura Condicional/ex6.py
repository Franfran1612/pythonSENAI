#Solicite ao usuário três números inteiros
# mostre o maior deles.

num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
num3 = int(input("digite outro numero: "))
if num1 > num2:
    print("o numero ",num1, "é maior que",num2,)
elif num2 > num3:
    print("o numero" , num2, "é maior que",num3,)
elif num3 > num1:
    print("o numero", num3, "é maior que",num1, )
else:
  print("qual dos tres é maior que",)


