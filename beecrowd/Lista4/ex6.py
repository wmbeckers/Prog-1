def calcular_percentual_sucesso(jogadores):
    total_saques = 0
    total_bloqueios = 0
    total_ataques = 0
    saques_sucesso = 0
    bloqueios_sucesso = 0
    ataques_sucesso = 0

    for jogador in jogadores:
        nome = jogador[0]
        saques, bloqueios, ataques = map(int, jogador[1].split())
        saques_sucesso, bloqueios_sucesso, ataques_sucesso = map(int, jogador[2].split())

        total_saques += saques
        total_bloqueios += bloqueios
        total_ataques += ataques
        saques_sucesso += saques_sucesso
        bloqueios_sucesso += bloqueios_sucesso
        ataques_sucesso += ataques_sucesso

    percentual_saques = (saques_sucesso / total_saques) * 100
    percentual_bloqueios = (bloqueios_sucesso / total_bloqueios) * 100
    percentual_ataques = (ataques_sucesso / total_ataques) * 100

    print(f'Pontos de Saque: {percentual_saques:.2f} %.')
    print(f'Pontos de Bloqueio: {percentual_bloqueios:.2f} %.')
    print(f'Pontos de Ataque: {percentual_ataques:.2f} %.')