def calculo_imc(altura, peso):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

altura = float(input("Digite a altura em metros: "))
peso = float(input("Digite o peso em kg: "))
categoria = calculo_imc(altura, peso)
print(f"IMC: {peso / (altura ** 2):.2f}, Categoria: {categoria}")
