"""80% no beecrowd, alguma coisa errada nessa porraaaaaaaaaaaaa"""

def construir_matriz(N):
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            if i == j:
                linha.append(1)
            else:
                linha.append(2)
        matriz.append(linha)
    return matriz

while True:
    N = int(input())
    if N == 0:
        break
    matriz = construir_matriz(N)
    for linha in matriz:
        for elemento in linha:
            print(f'{elemento:3}', end=' ')
        print()
    print()