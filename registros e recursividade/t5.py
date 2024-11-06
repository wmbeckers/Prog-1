def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def main():
    numero = int(input("Digite um valor inteiro positivo: "))
    if numero < 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        resultado = fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}")

if __name__ == "__main__":
    main()