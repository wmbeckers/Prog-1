#Considere um vetor de números inteiros com capacidade de 10 valores. Escreva um algoritmo que leia os
#valores do usuário e armazene no vetor e então implemente um procedimento recursivo que imprime os
#valores do vetor na ordem inversa (da última posição para a primeira).
def read_values():
    values = []
    for _ in range(10):
        value = int(input("Enter an integer: "))
        values.append(value)
    return values

def print_reverse(values, index):
    if index < 0:
        return
    print(values[index])
    print_reverse(values, index - 1)

def main():
    values = read_values()
    print("Values in reverse order:")
    print_reverse(values, len(values) - 1)

if __name__ == "__main__":
    main()