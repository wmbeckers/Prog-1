def calcular_notas_moedas(valor):
    # Notas
    notas_100 = valor // 100
    valor %= 100
    notas_50 = valor // 50
    valor %= 50
    notas_20 = valor // 20
    valor %= 20
    notas_10 = valor // 10
    valor %= 10
    notas_5 = valor // 5
    valor %= 5
    notas_2 = valor // 2
    valor %= 2

    # Moedas
    moedas_1 = valor // 1
    valor %= 1
    moedas_050 = valor // 0.50
    valor %= 0.50
    moedas_025 = valor // 0.25
    valor %= 0.25
    moedas_010 = valor // 0.10
    valor %= 0.10
    moedas_005 = valor // 0.05
    valor %= 0.05
    moedas_001 = round(valor / 0.01)  # Arredondar para evitar problemas de precisão

    print("NOTAS:")
    print(f"{int(notas_100)} nota(s) de R$ 100.00")
    print(f"{int(notas_50)} nota(s) de R$ 50.00")
    print(f"{int(notas_20)} nota(s) de R$ 20.00")
    print(f"{int(notas_10)} nota(s) de R$ 10.00")
    print(f"{int(notas_5)} nota(s) de R$ 5.00")
    print(f"{int(notas_2)} nota(s) de R$ 2.00")

    print("MOEDAS:")
    print(f"{int(moedas_1)} moeda(s) de R$ 1.00")
    print(f"{int(moedas_050)} moeda(s) de R$ 0.50")
    print(f"{int(moedas_025)} moeda(s) de R$ 0.25")
    print(f"{int(moedas_010)} moeda(s) de R$ 0.10")
    print(f"{int(moedas_005)} moeda(s) de R$ 0.05")
    print(f"{int(moedas_001)} moeda(s) de R$ 0.01")

# Leitura do valor de entrada
valor = float(input("\nInsira o valor: R$ "))
calcular_notas_moedas(valor)
