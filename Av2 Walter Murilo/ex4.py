def ler_matriz(arquivo):
    matriz = []
    with open(arquivo, 'r') as f:
        for linha in f:
            valores = linha.split()
            linha_matriz = [float(valor) for valor in valores]
            matriz.append(linha_matriz)
    return matriz

def transpor_matriz(matriz):
    matriz_transposta = []
    for i in range(len(matriz[0])):
        linha_transposta = []
        for j in range(len(matriz)):
            linha_transposta.append(matriz[j][i])
        matriz_transposta.append(linha_transposta)
    return matriz_transposta

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

arquivo_entrada = 'ex4.txt'
matriz_original = ler_matriz(arquivo_entrada)
matriz_transposta = transpor_matriz(matriz_original)

print('Matriz original:')
imprimir_matriz(matriz_original)

print('Matriz transposta:')
imprimir_matriz(matriz_transposta)