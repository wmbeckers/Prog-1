def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

n = int(input())

for _ in range(n):
    x = int(input())
    if is_perfect_number(x):
        print(f"{x} eh perfeito")
    else:
        print(f"{x} não eh perfeito")
