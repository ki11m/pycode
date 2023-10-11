import random
import time
import copy

def generate_random_list(length):
    return [random.randint(1, 1000) for _ in range(length)]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 测试不同长度的随机数列
list_lengths = [10, 100, 1000, 10000]
sorting_algorithms = {
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort
}

for length in list_lengths:
    random_list = generate_random_list(length)
    for algorithm_name, sorting_algorithm in sorting_algorithms.items():
        arr_copy = copy.deepcopy(random_list)
        start_time = time.time()
        sorting_algorithm(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{algorithm_name} on a list of length {length}: {execution_time:.6f} seconds\n")
