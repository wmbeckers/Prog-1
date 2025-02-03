idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo (feminino/masculino): ")

if sexo.lower() == 'feminino':
    if idade >= 62:
        print("Você já pode se aposentar.")
    else:
        print("Você ainda não pode se aposentar.")
elif sexo.lower() == 'masculino':
    if idade >= 65:
        print("Você já pode se aposentar.")
    else:
        print("Você ainda não pode se aposentar.")