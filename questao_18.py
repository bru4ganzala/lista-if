# 18. Faça um programa para verificar se um determinado número inteiro é divisível por 3 
# ou por 5, mas não simultaneamente pelos dois.

def verificar_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 != 0:
        print(numero, "é divisível por 3, mas não por 5.")
    elif numero % 5 == 0 and numero % 3 != 0:
        print(numero, "é divisível por 5, mas não por 3.")
    else:
        print(numero, "não é divisível por 3 nem por 5, ou é divisível por ambos.")

def main():
    numero = int(input("Digite um número inteiro: "))
    verificar_divisibilidade(numero)

main()