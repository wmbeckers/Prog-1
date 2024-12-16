#2. Números Ímpares
#• Escreva um programa que utilize um laço while para imprimir os números ímpares de 1 a 20

num = 1
while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1