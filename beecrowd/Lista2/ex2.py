values = input("Digite os valores de A, B e C separados por espaço: ").split()
A = float(values[0])
B = float(values[1])
C = float(values[2])

delta = B**2 - 4*A*C
if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    x1 = (-B + (delta)**0.5) / (2*A)
    x2 = (-B - (delta)**0.5) / (2*A)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")