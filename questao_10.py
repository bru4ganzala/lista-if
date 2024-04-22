# 10. Escreva um programa que leia um número inteiro maior do que zera e devolva, na 
# tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá 
# o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa 
# terminará com a mensagem “Número inválido”.

def soma_algarismos(numero):
    soma = 0
    while numero > 0:
        ultimo_digito = numero % 10
        soma += ultimo_digito
        numero //= 10
    return soma

def numero_valido(numero):
    return numero > 0

def main():
    numero = int(input("Digite um número inteiro maior do que zero: "))
    
    if numero_valido(numero):
        resultado = soma_algarismos(numero)
        print("A soma dos algarismos é:", resultado)
    else:
        print("Número inválido")

main()