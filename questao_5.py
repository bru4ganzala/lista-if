# 5. Faça um programa que receba um número inteiro e verificado se este número é par ou 
# ímpar

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")