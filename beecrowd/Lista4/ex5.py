N = int(input())

X = list(map(int, input().split()))

menor_valor = min(X)
posicao = X.index(menor_valor)

print("Menor valor:", menor_valor)
print("Posicao:", posicao)