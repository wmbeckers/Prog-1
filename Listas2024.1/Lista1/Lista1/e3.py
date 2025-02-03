v1 = input('Dê o primeiro valor\n')
v2 = input('Dê o segundo valor\n')
v3 = input('Dê o tercero valor\n')
v1 = int(v1)
v2 = int(v2)
v3 = int(v3)
if (v1 > v2 and v1 > v3):
    print(v1, 'é o maior valor\n')
elif (v2 > v1 and v2 > v3):
    print(v2, 'é o maior valor\n')
elif (v3 > v1 and v3 > v2):
    print(v3, 'é o maior valor\n')
