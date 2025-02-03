# 3. Calculadora de IMC
# • Escreva um programa que solicite o peso e a altura do usúario e calcule o Índice de Massa Corporal (IMC).

weight = float(input("Insira o seu peso em Kilogramas: "))
height = float(input("Insira a sua altura em Metros: "))
IMC = weight/height**2
IMC_f = "{:.2f}".format(IMC)
print(f"O IMC de uma pessoa de {weight} Kilogramas e {height} de altura é de {IMC_f}!")