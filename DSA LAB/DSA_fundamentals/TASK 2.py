import time
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]
def measure_time(func, n):
    start_time = time.perf_counter()
    result = func(n)
    end_time = time.perf_counter()
    return result, end_time - start_time
n_values = [10, 20, 30, 40]
print("\nExecution Time Comparison (seconds)")
print("n\tRecursive\tIterative\tMemoized Recursive")
print("-"*50)
for n in n_values:
    _, time_recursive = measure_time(fibonacci_recursive, n)
    _, time_iterative = measure_time(fibonacci_iterative, n)
    _, time_memoized  = measure_time(lambda x: fibonacci_memoized(x, {}), n)
    print(f"{n}\t{time_recursive:.6f}\t\t{time_iterative:.6f}\t\t{time_memoized:.6f}")
