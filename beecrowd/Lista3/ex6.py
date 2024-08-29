n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if y != 0:
        resultado = x / y
        print(f'{resultado:.1f}')
    else:
        print("divisao impossivel")
