# 9. Cálculo do Valor das Parcelas
# • Escreva um programa que solicite o valor à vista de um produto e o número de parcelas, e calcule o valor das parcelas que irá pagar

prod = float(input("Qual o valor do produto? "))
parc = float(input("Em quantas parcelas você deseja pagar? "))
val_parc = prod / parc 
print(f"Cada parcela será de {val_parc}$!")