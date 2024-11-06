word = input("Insira uma palavra ou frase: ")

if len(word) % 2 == 0:
    result = ''.join(['*' if i % 2 != 0 else char for i, char in enumerate(word)])
else:
    result = ''.join(['*' if i % 2 == 0 else char for i, char in enumerate(word)])

print(result)