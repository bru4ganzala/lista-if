# 14. Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia 
# da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e 
# assim por diante.

def imprimir_dia_semana(numero):
    dias_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }

    if 1 <= numero <= 7:
        dia = dias_semana[numero]
        print("O dia da semana correspondente a", numero, "é", dia)
    else:
        print("Número inválido. Por favor, insira um número entre 1 e 7.")

def main():
    numero = int(input("Digite um número inteiro entre 1 e 7: "))
    imprimir_dia_semana(numero)

main()