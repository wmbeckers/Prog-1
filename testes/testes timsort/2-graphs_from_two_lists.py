import matplotlib.pyplot as plt

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [float(line.strip()) for line in file]
    return numbers

def plot_numbers(file1, file2):
    numbers1 = read_numbers_from_file(file1)
    numbers2 = read_numbers_from_file(file2)
    
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.plot(numbers1, label='Sorted Numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Sorted Numbers')
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.plot(numbers2, label='Unsorted Numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Unsorted Numbers')
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.plot(numbers1, label='Sorted Numbers')
    plt.plot(numbers2, label='Unsorted Numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Both Lists')
    plt.legend()

    plt.tight_layout()
    plt.show()

file1 = 'sorted_numbers.txt'
file2 = 'unsorted_numbers.txt'

plot_numbers(file1, file2)