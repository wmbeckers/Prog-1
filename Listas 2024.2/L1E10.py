# 10. Conversão de Idade para Dias
# • Escreva um programa que solicite a idade do usuário em anos e a converta para dias, considerando anos bissextos

age = int(input("Insira a sua idade: "))
age_in_days = int(age * 365.25)
print("Você já viveu {} dias!".format(age_in_days))
