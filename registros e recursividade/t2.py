def contar_crescente(n, atual=1):
    if atual > n:
        return
    print(atual)
    contar_crescente(n, atual + 1)

# Solicita ao usuário um valor inteiro positivo
n = int(input("Digite um valor inteiro positivo: "))

# Verifica se o valor é positivo
if n > 0:
    contar_crescente(n)
else:
    print("Por favor, digite um valor inteiro positivo.")