# 8. Cálculo de Impostos sobre Compras
# • Um sistema de e-commerce precisa calcular o imposto sobre as compras realizadas. Escreva um
# programa que utilize um laço for para registrar o valor de 5 compras realizadas. O imposto
# será calculado da seguinte forma:
# – Se o valor da compra for menor que 100 reais, o imposto é de 5%.
# – Se o valor for entre 100 e 500 reais, o imposto é de 10%.
# – Se o valor for maior que 500 reais, o imposto é de 15%.
# O programa deve imprimir o valor do imposto de cada compra e o total de impostos pagos

compras = []

for i in range(5):
    valor = float(input(f"Digite o valor da compra {i+1}: "))
    compras.append(valor)

total_impostos = 0

for valor in compras:
    if valor < 100:
        imposto = valor * 0.05
    elif 100 <= valor <= 500:
        imposto = valor * 0.10
    else:
        imposto = valor * 0.15
    
    total_impostos += imposto
    print(f"Valor da compra: R${valor:.2f} - Imposto: R${imposto:.2f}")

print(f"Total de impostos pagos: R${total_impostos:.2f}")
