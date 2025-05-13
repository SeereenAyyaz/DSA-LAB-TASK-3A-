def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# Measure time for Quick Sort and Merge Sort
quick_sort_times = []
merge_sort_times = []

for size in input_sizes:
    arr = random.sample(range(size*10), size)
    quick_sort_times.append(measure_time(quick_sort, arr[:]))
    merge_sort_times.append(measure_time(merge_sort, arr[:]))

plt.plot(input_sizes, quick_sort_times, label="Quick Sort")
plt.plot(input_sizes, merge_sort_times, label="Merge Sort")
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Quick Sort vs Merge Sort')
plt.legend()
plt.show()
