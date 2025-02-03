def conta_digitos(numero):
    return len(str(abs(numero)))

numero = int(input("Digite um número: "))
print(conta_digitos(numero))