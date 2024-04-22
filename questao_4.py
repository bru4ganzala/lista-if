# 4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# a. O número digitado ao quadrado
# b. A raiz quadrada do número digitado

import math

numero = float(input("Digite um número: "))

if numero > 0:
    quadrado = numero ** 2
    raiz_quadrada = math.sqrt(numero)
    
    print("O número ao quadrado é:", quadrado)
    print("A raiz quadrada do número é:", raiz_quadrada)
else:
    print("O número não é positivo. Não é possível calcular o quadrado ou a raiz quadrada.")