# 6. Conversão de Distância
# • Escreva um programa que solicite uma distância em quilômetros e a converta para milhas.

km = float(input("Dê a distância em Quilômetros: "))
mi = (km * 0.609)
mi_f = "{:.2f}".format(mi)
print(f"{km} Quilômetros equivalem a {mi_f} milhas!")