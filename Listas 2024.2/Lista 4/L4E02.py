def numero_perfeito(n):
    if n < 2:
        return False
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    return soma_divisores == n

n = int(input("Digite um número: "))
print(numero_perfeito(n))
