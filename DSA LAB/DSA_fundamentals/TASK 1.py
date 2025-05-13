import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

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

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
random_list = [random.randint(1, 10000) for _ in range(1000)]

list_for_bubble = random_list.copy()
list_for_merge = random_list.copy()
list_for_quick = random_list.copy()

start_time = time.time()
bubble_sort(list_for_bubble)
bubble_sort_time = time.time() - start_time

start_time = time.time()
merge_sort(list_for_merge)
merge_sort_time = time.time() - start_time

start_time = time.time()
quick_sort(list_for_quick)
quick_sort_time = time.time() - start_time

print("\nExecution Time Comparison (in seconds):")
print("---------------------------------------")
print(f"Bubble Sort : {bubble_sort_time:.6f} sec")
print(f"Merge Sort  : {merge_sort_time:.6f} sec")
print(f"Quick Sort  : {quick_sort_time:.6f} sec")
algorithms = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
times = [bubble_sort_time, merge_sort_time, quick_sort_time]
plt.figure(figsize=(8, 5))
plt.bar(algorithms, times, color=['red', 'green', 'blue'])
plt.title('Sorting Algorithms Execution Time')
plt.xlabel('Algorithms')
plt.ylabel('Time (seconds)')
plt.grid(axis='y')
plt.show()
