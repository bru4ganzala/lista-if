# 23. Escreva um programa que, dada a idade de um atleta da categoria bocha rolada em 
# cancha de terra, classifique-o em uma das seguintes categorias:
# Categoria Idade
# Infantil A 5 a 7
# Infantil B 8 a 10
# Juvenil A 11 a 13
# Juvenil B 14 a 17
# Sênior Maiores de 18 anos

def classificar_atleta(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    else:
        return "Sênior"

idade = int(input("Digite a idade do atleta: "))

categoria = classificar_atleta(idade)
print("O atleta está na categoria:", categoria)
