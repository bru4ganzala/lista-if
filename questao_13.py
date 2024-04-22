# 13. A nota final de um estudante é calculada a partir de três notas atribuídas entre o 
# intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação 
# semestral e a um exame final. A média das três notas mencionadas anteriormente 
# obedece aos pesos: Trabalho de laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. 
# De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 
# 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações 
# necessárias.

def calcular_nota_final(nota_lab, nota_semestral, nota_final):
    peso_lab = 2
    peso_semestral = 3
    peso_final = 5

    nota_final = (nota_lab * peso_lab + nota_semestral * peso_semestral + nota_final * peso_final) / (peso_lab + peso_semestral + peso_final)
    return nota_final

def verificar_status(nota_final):
    if nota_final < 3.0:
        return "Reprovado"
    elif nota_final < 5.0:
        return "Em recuperação"
    else:
        return "Aprovado"

nota_lab = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
nota_semestral = float(input("Digite a nota da avaliação semestral (0 a 10): "))
nota_final = float(input("Digite a nota do exame final (0 a 10): "))

nota_final_aluno = calcular_nota_final(nota_lab, nota_semestral, nota_final)

status = verificar_status(nota_final_aluno)

# Exibe o resultado na 
print("A nota final do aluno é:", nota_final_aluno)
print("O aluno está", status)