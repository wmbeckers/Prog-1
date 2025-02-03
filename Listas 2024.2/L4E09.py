def serie_potencias(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i ** 2
    return soma

n = int(input("Digite um número inteiro: "))
print(f"A soma da série de potências até {n} é: {serie_potencias(n)}")