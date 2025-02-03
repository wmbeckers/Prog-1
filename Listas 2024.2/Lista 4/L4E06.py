def conta_consoantes(s):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in s.lower():
        if char in consoantes:
            count += 1
    return count

# Recebe a string do usuário
string = input("Digite uma string: ")
print(f"Número de consoantes: {conta_consoantes(string)}")