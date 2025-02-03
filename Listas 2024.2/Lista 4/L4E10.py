def celsius_para_kelvin(celsius):
    return celsius + 273.15

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_kelvin = celsius_para_kelvin(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_kelvin}K")