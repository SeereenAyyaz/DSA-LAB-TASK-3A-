import heapq

def heap_sort(arr):
    heapq.heapify(arr)  
    return [heapq.heappop(arr) for _ in range(len(arr))]
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
heap_sort_times = []
counting_sort_times = []

for size in input_sizes:
    arr = random.sample(range(size*10), size)
    heap_sort_times.append(measure_time(heap_sort, arr[:]))
    counting_sort_times.append(measure_time(counting_sort, arr[:]))

plt.plot(input_sizes, heap_sort_times, label="Heap Sort")
plt.plot(input_sizes, counting_sort_times, label="Counting Sort")
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Heap Sort vs Counting Sort')
plt.legend()
plt.show()
