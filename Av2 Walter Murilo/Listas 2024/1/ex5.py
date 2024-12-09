# 5. Conversão de Horas para Minutos
# • Escreva um programa que solicite uma quantidade de horas e a converta para minutos.

hours = float(input("Dê uma quantidade de horas: "))
min = (hours * 60)
min_f = "{:.2f}".format(min)
print(f"{hours} equivalem a {min_f} minutos!")