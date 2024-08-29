valores = []
for i in range(6):
    valor = float(input("Insira os valores: "))
    valores.append(valor)
positivos = 0
soma_positivos = 0
for valor in valores:
    if valor > 0:
        positivos += 1
        soma_positivos += valor
media_positivos = soma_positivos / positivos
print(positivos, "valores positivos")
print(f'{media_positivos:.1f}')