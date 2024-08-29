"""95% no beecrowd, pouca coisa está diferente"""

N = int(input())
M, L = map(int, input().split())

baralho_marcos = []
for _ in range(M):
    baralho_marcos.append(list(map(int, input().split())))

baralho_leonardo = []
for _ in range(L):
    baralho_leonardo.append(list(map(int, input().split())))

CM, CL = map(int, input().split())
A = int(input())

if baralho_marcos[CM-1][A-1] > baralho_leonardo[CL-1][A-1]:
    print("Marcos")
elif baralho_marcos[CM-1][A-1] < baralho_leonardo[CL-1][A-1]:
    print("Leonardo")
else:
    print("Empate")
