def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Digite um número inteiro maior ou igual a zero: "))
    if n < 0:
        print("O número deve ser maior ou igual a zero.")
    else:
        print(f"O valor correspondente da sequência de Fibonacci é: {fibonacci(n)}")

if __name__ == "__main__":
    main()