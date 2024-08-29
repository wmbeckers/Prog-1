while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    
    if m > n:
        m, n = n, m
    
    sequence = range(m, n+1)
    sequence_sum = sum(sequence)
    
    print(' '.join(map(str, sequence)), 'Sum=' + str(sequence_sum))