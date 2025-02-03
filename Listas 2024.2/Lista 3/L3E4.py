#4. Tabuada
#• Escreva um programa que peça ao usuário um número e imprima a tabuada desse número de
#1 a 10 utilizando um laço for.
#• Exemplo de Entrada:
#5
#• Exemplo de Sa´ıda Esperada:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50

numero = int(input("Digite um número: "))

for i in range(1, 10 + 1):
    print(f"{numero} x {i} = {numero * i}")