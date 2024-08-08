loop = 1
oper = 0

while loop == 1:

    x = input("Pressione 9 para cancelar a operação.\nCaso deseje continuar, pressione qualquer outra tecla\n")
    if x == "9":
        break

    num1 = input("Selecione o primeiro número: ")
    
    oper = input("Selecione o operador:\n+: para adição\n-: para subtração\n*: para multiplicação\n/: para divisão\n**: para pontenciação\n")

    num2 = input("Selecione o segundo número: ")
    
    if oper == "+":
        result = float(num1) + float(num2)
    elif oper == "-":
        result = float(num1) - float(num2)
    elif oper == "*":
        result = float(num1) * float(num2)
    elif oper == "/":
        result = float(num1) / float(num2)
    elif oper == "**":
        result = float(num1) ** float(num2)
    else:
        print("Operador inválido!")

    print ("O resultado de " + str(num1) + str(oper) + str(num2) + " é " + str(result))

    print("\nPressione 9 para sair.")
