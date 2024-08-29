notas = list(map(float, input().split()))
media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3] * 1) / 10
print("Media:", format(media, ".1f"))
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Nota do exame: "))
    media_final = (media + nota_exame) / 2
    print("Media final:", format(media_final, ".1f"))
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")