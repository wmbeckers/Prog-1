def contagem_regressiva(n):
    if n <= 0:
        return
    print(n)
    contagem_regressiva(n - 1)

def main():
    n = int(input("Digite um valor inteiro positivo: "))
    if n > 0:
        contagem_regressiva(n)
    else:
        print("Por favor, digite um valor inteiro positivo.")

if __name__ == "__main__":
    main()