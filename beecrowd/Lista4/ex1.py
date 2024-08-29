X = []
for i in range(10):
    X.append(int(input()))

for i in range(10):
    if X[i] <= 0:
        X[i] = 1

for i in range(10):
    print(f"X[{i}] = {X[i]}")
