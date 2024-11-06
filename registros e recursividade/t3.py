def soma_recursiva(a, b):
    if b == 0:
        return a
    else:
        return soma_recursiva(a + 1, b - 1)

def main():
    try:
        a = int(input("Digite o primeiro valor inteiro positivo: "))
        b = int(input("Digite o segundo valor inteiro positivo: "))
        if a < 0 or b < 0:
            raise ValueError("Os valores devem ser inteiros positivos.")
        resultado = soma_recursiva(a, b)
        print(f"A soma de {a} e {b} é: {resultado}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()