def classificacao_nota(nota):
    if 90 <= nota <= 100:
        return 'A'
    elif 80 <= nota < 90:
        return 'B'
    elif 70 <= nota < 80:
        return 'C'
    elif 60 <= nota < 70:
        return 'D'
    elif 0 <= nota < 60:
        return 'F'
    else:
        return 'Nota inválida'

nota = float(input("Digite a nota: "))
print(f'A classificação da nota {nota} é: {classificacao_nota(nota)}')