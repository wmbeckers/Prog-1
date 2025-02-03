def conversao_tempo(segundos):
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_finais = segundos_restantes % 60
    return horas, minutos, segundos_finais

segundos = int(input("Digite a quantidade de segundos: "))
horas, minutos, segundos_finais = conversao_tempo(segundos)
print(f"{horas} horas, {minutos} minutos e {segundos_finais} segundos")