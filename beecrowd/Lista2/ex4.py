cod_item, quantidade = map(int, input("Insira o codigo do item e a quantidade (separados por espaço): ").split())
precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
total = precos[cod_item] * quantidade
print("Total: R$ {:.2f}".format(total))
