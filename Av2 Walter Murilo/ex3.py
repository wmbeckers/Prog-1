def calculate_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

def calculate_upper_diagonal_sum(matrix):
    upper_diagonal_sum = 0
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            upper_diagonal_sum += matrix[i][j]
    return upper_diagonal_sum

def calculate_lower_diagonal_sum(matrix):
    lower_diagonal_sum = 0
    for i in range(len(matrix)):
        for j in range(i):
            lower_diagonal_sum += matrix[i][j]
    return lower_diagonal_sum

matrix = []
for i in range(4):
    row = []
    for j in range(4):
        num = float(input(f"Insira o número real para a posição [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

diagonal_sum = calculate_diagonal_sum(matrix)
if diagonal_sum % 2 == 0:
    diagonal_type = "diagonal inferior"
    diagonal_sum = calculate_lower_diagonal_sum(matrix)
else:
    diagonal_type = "diagonal superior"
    diagonal_sum = calculate_upper_diagonal_sum(matrix)

print("Cálculo do somatório da", diagonal_type.upper())
print("Somatório =", diagonal_sum)