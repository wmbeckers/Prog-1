numbers = [int(input("Digite um número: ")) for _ in range(100)]

max_value = max(numbers)
max_position = numbers.index(max_value)
print(f"Maior valor: {max_value}")
print(f"Posição: {max_position+1}")