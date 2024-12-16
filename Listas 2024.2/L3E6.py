#6. Controle de Estoque de Produtos
#• Uma loja possui um estoque de 15 produtos. Escreva um programa que utilize um laço while
#para verificar a quantidade de cada produto no estoque. Para cada produto, o programa deve
#perguntar ao usuário a quantidade disponível. Se a quantidade for menor ou igual a 5, o
#programa deve imprimir "Produto em falta, precisa repor". Caso contrário, o programa deve
#imprimir "Estoque suficiente".

num_produtos = 15
contador = 0

while contador < num_produtos:
    quantidade = int(input(f"Digite a quantidade disponível do produto {contador + 1}: "))
    if quantidade <= 5:
        print("Produto em falta, precisa repor")
    else:
        print("Estoque suficiente")
    contador += 1