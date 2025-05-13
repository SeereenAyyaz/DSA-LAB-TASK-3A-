def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1  
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  
import random
import time

# Measure execution time for each search algorithm
def measure_time(search_algorithm, arr, target):
    start_time = time.time()
    search_algorithm(arr, target)
    end_time = time.time()
    return end_time - start_time

input_sizes = [1000, 5000, 10000]
for size in input_sizes:
    unsorted_arr = random.sample(range(size*10), size)
    sorted_arr = sorted(unsorted_arr)
    target = random.choice(unsorted_arr)
    print(f"Input size: {size}")
    print(f"Linear Search Time: {measure_time(linear_search, unsorted_arr, target)} seconds")
    print(f"Binary Search Time: {measure_time(binary_search, sorted_arr, target)} seconds")
    print("-" * 40)

