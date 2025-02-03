def media_tres_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    media = (num1 + num2 + num3) / 3
    return media

print("A média aritmética é:", media_tres_numeros())