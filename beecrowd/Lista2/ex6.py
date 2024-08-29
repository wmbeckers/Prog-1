coordenadas = input("Digite os valores de x e y separados por espaço: ")
x, y = map(float, coordenadas.split())

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
elif x == 0 and y == 0:
    print("O ponto está na origem.")
elif x == 0:
    print("O ponto está sobre o eixo Y.")
elif y == 0:
    print("O ponto está sobre o eixo X.")