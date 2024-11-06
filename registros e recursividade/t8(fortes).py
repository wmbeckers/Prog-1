def hanoi(n, torreA, torreB, torreAux):
    if n == 1:
        print(f"Desloca disco 1 de {torreA} para {torreB}")
        return
    # Move n-1 discos de torreA para torreAux usando torreB como auxiliar
    hanoi(n - 1, torreA, torreAux, torreB)
    # Move o disco n de torreA para torreB
    print(f"Desloca disco {n} de {torreA} para {torreB}")
    # Move os n-1 discos de torreAux para torreB usando torreA como auxiliar
    hanoi(n - 1, torreAux, torreB, torreA)

# Número de discos
n = 4  # Você pode mudar o valor de n para o número desejado de discos
hanoi(n, 'A', 'B', 'C')