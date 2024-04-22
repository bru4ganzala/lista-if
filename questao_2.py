# 2. Leia um número fornecido pelo usuário. Se esse numero for positivo, calcule a raiz 
# quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que 
# o número é inválido.

import math

numero = float(input("Digite um número: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
else:
    print("Número inválido. Por favor, insira um número positivo.")