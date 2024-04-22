# 15. Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês 
# correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.

def obter_nome_mes(numero):
    if numero == 1:
        return "janeiro"
    elif numero == 2:
        return "fevereiro"
    elif numero == 3:
        return "março"
    elif numero == 4:
        return "abril"
    elif numero == 5:
        return "maio"
    elif numero == 6:
        return "junho"
    elif numero == 7:
        return "julho"
    elif numero == 8:
        return "agosto"
    elif numero == 9:
        return "setembro"
    elif numero == 10:
        return "outubro"
    elif numero == 11:
        return "novembro"
    elif numero == 12:
        return "dezembro"
    else:
        return "Número inválido"

numero_mes = int(input("Digite um número entre 1 e 12 para obter o nome do mês correspondente: "))

nome_mes = obter_nome_mes(numero_mes)

print("O mês correspondente ao número", numero_mes, "é", nome_mes)