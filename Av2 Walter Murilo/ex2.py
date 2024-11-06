word = input("Insira uma palavra ou frase: ")

rev_word = word[::-1]

for i in range(len(word)):
    swap_word = word[:i] + rev_word[i] + word[i+1:]
    print(swap_word[::-1])