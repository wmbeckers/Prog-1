def print_vector(name, vector):
    for i in range(len(vector)):
        print(f"{name}[{i}] = {vector[i]}")

def main():
    data = []
    for _ in range(15):
        data.append(int(input().strip()))

    par = []
    impar = []

    for num in data:
        if num % 2 == 0:
            par.append(num)
            if len(par) == 5:
                print_vector("par", par)
                par = []
        else:
            impar.append(num)
            if len(impar) == 5:
                print_vector("impar", impar)
                impar = []

    if impar:
        print_vector("impar", impar)
    if par:
        print_vector("par", par)

if __name__ == "__main__":
    main()
