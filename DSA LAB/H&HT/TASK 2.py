import matplotlib.pyplot as plt
from collections import defaultdict
def custom_hash(key):
    return sum(ord(c) for c in key) % 10

keys = ["hello", "world", "test", "hash", "function", "collision", "data"]
hash_table = defaultdict(int)
for key in keys:
    hash_table[custom_hash(key)] += 1
builtin_hash_table = defaultdict(int)
for key in keys:
    builtin_hash_table[hash(key) % 10] += 1
plt.figure(figsize=(10, 5))
plt.hist(hash_table.values(), bins=range(1, max(hash_table.values()) + 1), alpha=0.5, label="Custom Hash")
plt.hist(builtin_hash_table.values(), bins=range(1, max(builtin_hash_table.values()) + 1), alpha=0.5, label="Builtin Hash")
plt.legend()
plt.title("Hash Distribution Comparison")
plt.xlabel("Number of Collisions")
plt.ylabel("Frequency")
plt.show()
