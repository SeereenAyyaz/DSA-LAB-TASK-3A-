import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  
    prev = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i  
    
    return -1  
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1  
jump_search_times = []
interpolation_search_times = []
binary_search_times = []

input_sizes = [1000, 5000, 10000]

for size in input_sizes:
    sorted_arr = sorted(random.sample(range(size*10), size))
    target = random.choice(sorted_arr)
    
    jump_search_times.append(measure_time(jump_search, sorted_arr, target))
    interpolation_search_times.append(measure_time(interpolation_search, sorted_arr, target))
    binary_search_times.append(measure_time(binary_search, sorted_arr, target))

plt.plot(input_sizes, jump_search_times, label="Jump Search")
plt.plot(input_sizes, interpolation_search_times, label="Interpolation Search")
plt.plot(input_sizes, binary_search_times, label="Binary Search")
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Jump Search vs Interpolation Search vs Binary Search')
plt.legend()
plt.show()
