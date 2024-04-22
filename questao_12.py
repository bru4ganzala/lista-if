# 12. Faça um algoritmo que calcule a média ponderada das notas de 2 provas. A primeira 
# prova tem peso 1 e a segunda tem peso 2. Ao final, mostrar a média do aluno e indicar 
# se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual o superior 
# a 70 pontos.

def calcular_media_ponderada(nota1, nota2):
    peso1 = 1
    peso2 = 2

    media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
    return media_ponderada

def verificar_aprovacao(media):
    if media >= 70:
        return "Aprovado"
    else:
        return "Reprovado"

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media = calcular_media_ponderada(nota1, nota2)

resultado = verificar_aprovacao(media)

print("A média do aluno é:", media)
print("O aluno está", resultado)