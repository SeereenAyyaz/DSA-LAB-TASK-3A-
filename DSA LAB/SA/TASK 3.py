def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2  
    return binary_search(arr[i//2: min(i, n)], target)  
def fibonacci_search(arr, target):
    n = len(arr)
    fib_m_2 = 0  # (m-2)'th Fibonacci number
    fib_m_1 = 1  # (m-1)'th Fibonacci number
    fib = fib_m_1 + fib_m_2  # m'th Fibonacci number
    
    while fib < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib
        fib = fib_m_1 + fib_m_2
    
    offset = -1
    while fib > 1:
        i = min(offset + fib_m_2, n-1)
        
        if arr[i] < target:
            fib = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib - fib_m_1
            offset = i
        
        elif arr[i] > target:
            fib = fib_m_2
            fib_m_1 -= fib_m_2
            fib_m_2 = fib - fib_m_1
        
        else:
            return i
    
    if fib_m_1 and arr[offset+1] == target:
        return offset+1
    
    return -1
exponential_search_times = []
fibonacci_search_times = []

for size in input_sizes:
    sorted_arr = sorted(random.sample(range(size*10), size))
    target = random.choice(sorted_arr)
    
    exponential_search_times.append(measure_time(exponential_search, sorted_arr, target))
    fibonacci_search_times.append(measure_time(fibonacci_search, sorted_arr, target))

plt.plot(input_sizes, exponential_search_times, label="Exponential Search")
plt.plot(input_sizes, fibonacci_search_times, label="Fibonacci Search")
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Exponential Search vs Fibonacci Search')
plt.legend()
plt.show()
