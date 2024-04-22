# 17. Faça um programa que mostre ao usuário um menu com 4 opções de operações 
# matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu 
# programa então pede dois valores numéricos e realiza a operação, mostrando o 
# resultado e saind

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

def menu():
    print("Escolha a operação que deseja realizar:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def main():
    menu()
    escolha = int(input("Digite o número da operação desejada: "))

    if escolha < 1 or escolha > 4:
        print("Opção inválida!")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == 1:
        resultado = soma(num1, num2)
    elif escolha == 2:
        resultado = subtracao(num1, num2)
    elif escolha == 3:
        resultado = multiplicacao(num1, num2)
    elif escolha == 4:
        resultado = divisao(num1, num2)

    print("O resultado da operação é:", resultado)

if __name__ == "__main__":
    main()