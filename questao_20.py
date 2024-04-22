# 20. Leia a idade e o tempo de serviço de um trabalhador e escreve se ele pode ou não se 
# aposentar. As condições para aposentadoria são:
# a. Ter pelo menos 65 anos
# b. Ou ter trabalhado pelo menos 30 anos
# c. Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

def pode_aposentar(idade, tempo_de_servico):
    if idade >= 65 or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25):
        return True
    else:
        return False

idade = int(input("Digite a idade do trabalhador: "))
tempo_de_servico = int(input("Digite o tempo de serviço do trabalhador: "))

if pode_aposentar(idade, tempo_de_servico):
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador ainda não pode se aposentar.")