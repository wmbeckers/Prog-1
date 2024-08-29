X = int(input("Insira um valor inteiro: "))
Y = int(input("Insira outro valor inteiro: "))
if X > Y:
    X, Y = Y, X
soma = 0
for num in range(X+1, Y):
    if num % 2 != 0:
        soma += num
print(soma)