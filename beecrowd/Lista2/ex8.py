hora_inicial, hora_final = map(int, input("Digite a hora inicial e final do jogo (separadas por espaço): ").split())
if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
else:
    duracao = 24 - hora_inicial + hora_final
print(f"O JOGO DUROU {duracao} HORA(S)")    
