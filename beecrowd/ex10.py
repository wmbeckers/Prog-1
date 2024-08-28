idade_em_dias = int(input())
anos = idade_em_dias // 365
idade_em_dias %= 365
meses = idade_em_dias // 30
idade_em_dias %= 30
dias = idade_em_dias
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')