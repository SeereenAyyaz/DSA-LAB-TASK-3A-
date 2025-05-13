import heapq

def find_k_smallest(arr, k):
    heapq.heapify(arr)  
    result = []
    for _ in range(k):
        result.append(heapq.heappop(arr))
    return result

def find_k_largest(arr, k):
    max_heap = [-x for x in arr]  
    heapq.heapify(max_heap)
    result = []
    for _ in range(k):
        result.append(-heapq.heappop(max_heap))
    return result

# Test Cases
arr = [10, 4, 3, 20, 15, 7]
print("\nK Smallest and K Largest Elements Example:")
print(find_k_smallest(arr.copy(), 3))  
print(find_k_largest(arr.copy(), 2))   
