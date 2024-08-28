valor = float(input())
notas_100 = int(valor / 100)
valor %= 100
notas_50 = int(valor / 50)
valor %= 50
notas_20 = int(valor / 20)
valor %= 20
notas_10 = int(valor / 10)
valor %= 10
notas_5 = int(valor / 5)
valor %= 5
notas_2 = int(valor / 2)
valor %= 2
moedas_1 = int(valor / 1)
valor %= 1
moedas_0_50 = int(valor / 0.50)
valor %= 0.50
moedas_0_25 = int(valor / 0.25)
valor %= 0.25
moedas_0_10 = int(valor / 0.10)
valor %= 0.10
moedas_0_05 = int(valor / 0.05)
valor %= 0.05
moedas_0_01 = int(valor / 0.01)
print("NOTAS:")
print(f"{notas_100} nota(s) de R$ 100.00")
print(f"{notas_50} nota(s) de R$ 50.00")
print(f"{notas_20} nota(s) de R$ 20.00")
print(f"{notas_10} nota(s) de R$ 10.00")
print(f"{notas_5} nota(s) de R$ 5.00")
print(f"{notas_2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moedas_1} moeda(s) de R$ 1.00")
print(f"{moedas_0_50} moeda(s) de R$ 0.50")
print(f"{moedas_0_25} moeda(s) de R$ 0.25")
print(f"{moedas_0_10} moeda(s) de R$ 0.10")
print(f"{moedas_0_05} moeda(s) de R$ 0.05")
print(f"{moedas_0_01} moeda(s) de R$ 0.01")