#def determinar_reacao_sheldon(escolha_sheldon, escolha_raj):
#    if escolha_sheldon == escolha_raj:
#        return "De novo!"
#    elif (escolha_sheldon == "tesoura" and (escolha_raj == "papel" or escolha_raj == "lagarto")) or (escolha_sheldon == "papel" and (escolha_raj == "pedra" or escolha_raj == "Spock")) or (escolha_sheldon == "pedra" and (escolha_raj == "lagarto" or escolha_raj == "tesoura")) or (escolha_sheldon == "lagarto" and (escolha_raj == "Spock" or escolha_raj == "papel")) or (escolha_sheldon == "Spock" and (escolha_raj == "tesoura" or escolha_raj == "pedra")):
#        return "Bazinga!"
#    else:
#        return "Raj trapaceou!"
#def jogar_pedra_papel_tesoura_lagarto_spock():
#    t = int(input())
#    for i in range(t):
#        escolha_sheldon, escolha_raj = input().split()
#        reacao_sheldon = determinar_reacao_sheldon(escolha_sheldon, escolha_raj)
#        print(f"Caso #{i+1}: {reacao_sheldon}")
#jogar_pedra_papel_tesoura_lagarto_spock()

#acima nao aceito pelo beecrowd


# Regras do jogo como um dicionário
regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "Spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["Spock", "papel"],
    "Spock": ["tesoura", "pedra"]
}

# Lê o número de casos de teste
T = int(input().strip())

# Processa cada caso de teste
for t in range(1, T + 1):
    # Lê as escolhas de Sheldon e Raj
    sheldon, raj = input().strip().split()

    # Determina o resultado
    if sheldon == raj:
        resultado = "De novo!"
    elif raj in regras[sheldon]:
        resultado = "Bazinga!"
    else:
        resultado = "Raj trapaceou!"

    # Imprime o resultado no formato exigido
    print(f"Caso #{t}: {resultado}")
