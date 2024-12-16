# Verificação de Idade para Votação
# Um sistema precisa verificar se uma pessoa pode votar com base em sua idade. Escreva um
# programa que utilize um laço for para ler a idade de 10 pessoas. Se a idade for maior ou
# igual a 18, o sistema deve imprimir "Você pode votar"; caso contrário, deve imprimir "Você
# não pode votar".

for i in range(1, 10 + 1):
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        print("Você pode votar")
    else:
        print("Você não pode votar")