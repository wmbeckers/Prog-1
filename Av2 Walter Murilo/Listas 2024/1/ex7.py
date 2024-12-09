# 7. Média Aritmética
# • Escreva um programa que solicite três números ao usuário, calcule a média aritmética e exiba o resultado

v1 = float(input("Dê o primeiro número: "))
v2 = float(input("Dê o segundo número: "))
v3 = float(input("Dê o terceiro número: "))
MediaA = ((v1 + v2 + v3) / 3)
MediaA_f = "{:.2f}".format(MediaA)
print(f"A média entre {v1}, {v2}, {v3} é de {MediaA_f}!")