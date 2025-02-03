#7. Aprovado ou Reprovado
#• Um professor deseja calcular se seus alunos foram aprovados ou reprovados com base nas notas
#das provas. Escreva um programa que utilize um laço for para ler as notas de 10 alunos. Se a
#nota do aluno for maior ou igual a 7, o programa deve imprimir "Aprovado"; caso contrário,
#deve imprimir "Reprovado". O programa deve também verificar se a nota do aluno é maior
#que 10 ou menor que 0, e nesse caso imprimir "Nota inválida" e continuar para o próximo
#aluno

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    
    if nota < 0 or nota > 10:
        print("Nota inválida")
    elif nota >= 7:
        print("Aprovado")
    else:
        print("Reprovado")