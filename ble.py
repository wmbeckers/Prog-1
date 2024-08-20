hr = input('Indique a hora\n')
mn = input('Indique os minutos\n')
sg = input('Indique os segundos\n')

ssm = ((int(hr)*60+int(mn))*60)+int (sg)
print('fazem ', ssm, ' seg desde a meia noite')

## https://stackoverflow.com/questions/19821273/limiting-user-input-to-a-range-in-python
