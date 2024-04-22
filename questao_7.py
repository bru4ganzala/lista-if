# 7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois 
# números forem iguais, imprima a mensagem “Números iguais”.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Números iguais")