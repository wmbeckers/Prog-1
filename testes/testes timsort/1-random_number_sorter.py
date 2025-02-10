import numpy as np
from sklearn.utils import shuffle

def timsort(arr):
    min_run = 32
    n = len(arr)

    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(arr, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = np.array(arr[l:m+1]), np.array(arr[m+1:r+1])

        i, j, k = 0, 0, l
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size

    return arr

# Example usage
arr = shuffle(np.random.randint(0, 2048, 256))

# Write unsorted array to file
with open('/home/aluno/Documentos/prog1/unsorted_numbers.txt', 'w') as f:
    for num in arr:
        f.write(f"{num}\n")

sorted_arr = timsort(arr)

# Write sorted array to file
with open('/home/aluno/Documentos/prog1/sorted_numbers.txt', 'w') as f:
    for num in sorted_arr:
        f.write(f"{num}\n")

print("Files created successfully.")
