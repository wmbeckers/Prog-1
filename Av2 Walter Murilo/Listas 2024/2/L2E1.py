valor_gasto = float(input("Digite o valor gasto: R$ "))

if valor_gasto > 200:
    parcela = valor_gasto / 3
    print(f"Você pode parcelar a compra em 3x de R$ {parcela:.2f}")
else:
    parcela = valor_gasto / 2
    print(f"Você pode parcelar a compra em 2x de R$ {parcela:.2f}")