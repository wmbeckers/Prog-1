def calcular_duracao_evento(inicio, fim):
    inicio_hora, inicio_minuto, inicio_segundo = map(int, inicio.split(':'))
    fim_hora, fim_minuto, fim_segundo = map(int, fim.split(':'))
    duracao_segundos = (fim_hora * 3600 + fim_minuto * 60 + fim_segundo) - (inicio_hora * 3600 + inicio_minuto * 60 + inicio_segundo)
    dias = duracao_segundos // (24 * 3600)
    duracao_segundos %= (24 * 3600)
    horas = duracao_segundos // 3600
    duracao_segundos %= 3600
    minutos = duracao_segundos // 60
    duracao_segundos %= 60
    segundos = duracao_segundos
    return f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)'
dia_inicio = input().split()[1]
hora_inicio = input()
dia_fim = input().split()[1]
hora_fim = input()
duracao_evento = calcular_duracao_evento(hora_inicio, hora_fim)
print(duracao_evento)