import time
# Brute Force Method (O(n²))
def longest_substring_bruteforce(s):
    max_len = 0
    max_substr = ""
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) == len(substring):  
                if len(substring) > max_len:
                    max_len = len(substring)
                    max_substr = substring
    return max_substr, max_len

# Sliding Window Method (O(n))
def longest_substring_sliding_window(s):
    char_set = set()
    left = 0
    max_len = 0
    max_substr = ""
    
    for right in range(len(s)):
        while s[right] in char_set:  
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        
        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_substr = s[left:right+1]
    
    return max_substr, max_len

# Execution Time Comparison
# Test cases are provided below of each method
s = "abcabcbb"

# Measure time for Brute Force method
start_time = time.time()
result_bruteforce = longest_substring_bruteforce(s)
end_time = time.time()
bruteforce_time = end_time - start_time

# Measure time for Sliding Window method
start_time = time.time()
result_sliding_window = longest_substring_sliding_window(s)
end_time = time.time()
sliding_window_time = end_time - start_time

print("Brute Force Method: Longest Substring:", result_bruteforce[0], "Length:", result_bruteforce[1])
print("Execution Time (Brute Force):", bruteforce_time)
print("Sliding Window Method: Longest Substring:", result_sliding_window[0], "Length:", result_sliding_window[1])
print("Execution Time (Sliding Window):", sliding_window_time)

test_cases = [
    "abcabcbb",  # Expected Output: "abc", Length: 3
    "bbbbb",      # Expected Output: "b", Length: 1
    "pwwkew",     # Expected Output: "wke", Length: 3
    "dvdf",       # Expected Output: "vdf", Length: 3
]

for s in test_cases:
    print(f"Testing string: {s}")
    result_bruteforce = longest_substring_bruteforce(s)
    print(f"Brute Force: Longest Substring: {result_bruteforce[0]}, Length: {result_bruteforce[1]}")
    result_sliding_window = longest_substring_sliding_window(s)
    print(f"Sliding Window: Longest Substring: {result_sliding_window[0]}, Length: {result_sliding_window[1]}")
    print()
