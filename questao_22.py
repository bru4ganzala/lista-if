# 22. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado 
# possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%.; RJ 15%; MS 
# 8%). Faça um programa em que o usuário entre com o valor e o estado destino do 
# produto e o programa retorne o preço final do produto acrescido do imposto do 
# estado em que ele será vendido. Se o estado digitado não for valido, mostrar uma 
# mensagem de erro

def calcular_preco_final(valor, estado):
    impostos = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}
    if estado in impostos:
        taxa_imposto = impostos[estado]
        preco_final = valor * (1 + taxa_imposto)
        return preco_final
    else:
        return "Erro: Estado inválido!"

def main():
    valor_produto = float(input("Digite o valor do produto: "))
    estado_destino = input("Digite a sigla do estado destino (MG, SP, RJ ou MS): ").upper()

    preco_final = calcular_preco_final(valor_produto, estado_destino)
    print("Preço final do produto:", preco_final)

if __name__ == "__main__":
    main()
