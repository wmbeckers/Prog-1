"""nao adicionado ao beecrowd, mas funciona perfeitamente"""

par = []
impar = []

numeros = []

for _ in range(15):
    num = int(input())
    numeros.append(num)

for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")
