def calcular_duracao(inicio_dia, inicio_horario, fim_dia, fim_horario):
    inicio_dia = int(inicio_dia)
    fim_dia = int(fim_dia)
    inicio_horas, inicio_minutos, inicio_segundos = map(int, inicio_horario.split(" : "))
    fim_horas, fim_minutos, fim_segundos = map(int, fim_horario.split(" : "))
    
    inicio_total_segundos = inicio_dia * 86400 + inicio_horas * 3600 + inicio_minutos * 60 + inicio_segundos
    fim_total_segundos = fim_dia * 86400 + fim_horas * 3600 + fim_minutos * 60 + fim_segundos
    
    duracao_total_segundos = fim_total_segundos - inicio_total_segundos
    
    dias = duracao_total_segundos // 86400
    duracao_total_segundos %= 86400
    horas = duracao_total_segundos // 3600
    duracao_total_segundos %= 3600
    minutos = duracao_total_segundos // 60
    segundos = duracao_total_segundos % 60

    return dias, horas, minutos, segundos

inicio_dia = input().split()[1]
inicio_horario = input().strip()
fim_dia = input().split()[1]
fim_horario = input().strip()

dias, horas, minutos, segundos = calcular_duracao(inicio_dia, inicio_horario, fim_dia, fim_horario)

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")