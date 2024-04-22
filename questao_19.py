# 19. Dados três valores A, B, C, verificar se eles podem ser valores dos lados de um 
# triangulo e se forem, se é um triangulo escaleno, equilátero ou isóscele, considerando 
# os seguintes conceitos:

def verificar_tipo_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print("Os lados formam um triângulo equilátero.")
        elif a == b or a == c or b == c:
            print("Os lados formam um triângulo isósceles.")
        else:
            print("Os lados formam um triângulo escaleno.")
    else:
        print("Os lados fornecidos não podem formar um triângulo.")

def main():
    a = float(input("Digite o comprimento do primeiro lado do triângulo: "))
    b = float(input("Digite o comprimento do segundo lado do triângulo: "))
    c = float(input("Digite o comprimento do terceiro lado do triângulo: "))