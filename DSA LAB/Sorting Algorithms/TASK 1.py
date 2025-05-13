def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

import time
import random

# Measure execution time for different sizes
def measure_time(sorting_algorithm, arr):
    start_time = time.time()
    sorting_algorithm(arr)
    end_time = time.time()
    return end_time - start_time
input_sizes = [100, 500, 1000, 5000, 10000]
for size in input_sizes:
    arr = random.sample(range(size*10), size) 
    print(f"Input size: {size}")
    print(f"Bubble Sort Time: {measure_time(bubble_sort, arr[:])} seconds")
    print(f"Selection Sort Time: {measure_time(selection_sort, arr[:])} seconds")
    print(f"Insertion Sort Time: {measure_time(insertion_sort, arr[:])} seconds")
    print("-" * 40)

import matplotlib.pyplot as plt

input_sizes = [100, 500, 1000, 5000, 10000]
bubble_sort_times = []
selection_sort_times = []
insertion_sort_times = []

for size in input_sizes:
    arr = random.sample(range(size*10), size)
    bubble_sort_times.append(measure_time(bubble_sort, arr[:]))
    selection_sort_times.append(measure_time(selection_sort, arr[:]))
    insertion_sort_times.append(measure_time(insertion_sort, arr[:]))

plt.plot(input_sizes, bubble_sort_times, label="Bubble Sort")
plt.plot(input_sizes, selection_sort_times, label="Selection Sort")
plt.plot(input_sizes, insertion_sort_times, label="Insertion Sort")
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance Comparison')
plt.legend()
plt.show()
