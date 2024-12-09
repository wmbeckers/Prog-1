# 4. Cálculo de Área de um Círculo
# • Escreva um programa que solicite o raio de um círculo e calcule a área.

ray = float(input("Dê o raio de um círculo em centímetros: "))
area = (3.1415 * (ray ** 2))
area_f = "{:.2f}".format(area)
print(f"A área de um círculo com raio {ray} cm é de {area_f} centímetros quadrados!")