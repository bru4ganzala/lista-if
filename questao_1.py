#1. Faça um programa que receba dois números e mostra qual deles é o maior.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro número ({}) é maior que o segundo número ({})".format(num1, num2))
elif num2 > num1:
    print("O segundo número ({}) é maior que o primeiro número ({})".format(num2, num1))
else:
    print("Os dois números são iguais.")