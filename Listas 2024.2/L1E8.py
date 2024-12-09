# 8. Cálculo de Desconto
#• Escreva um programa que solicite o preço de um produto e a porcentagem de desconto, calcule o preço com desconto e exiba o resultado

preco = float(input("Qual o preço do produto? "))
desc = int(input("Quantos % o produto tem de desconto? "))
v_desc = (preco * desc / 100)
preco_d = preco - v_desc
print(f"O preço do produto foi de {preco} para {preco_d} com os {desc}% de desconto!")