A, B, C = map(float, input("Insira medidas para os lados de um triangulo, separadas por espaço: ").split())

if A < B:
    A, B = B, A
if A < C:
    A, C = C, A
if B < C:
    B, C = C, B

if A >= B + C:
    print("Nao forma triangulo")
else:
    print("Forma triangulo")
    if A != B and B != C and A != C:
        print("O triangulo é escaleno")
    else:
        print("O triangulo não é escaleno")