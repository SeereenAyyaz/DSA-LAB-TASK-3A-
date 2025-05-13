class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self.hash_function(key)
        new_node = Node(key, value)
        if not self.table[idx]:
            self.table[idx] = new_node
        else:
            current = self.table[idx]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node

    def get(self, key):
        idx = self.hash_function(key)
        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        idx = self.hash_function(key)
        current = self.table[idx]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[idx] = current.next
                return
            prev = current
            current = current.next

    def display(self):
        for idx, node in enumerate(self.table):
            print(f"Index {idx}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")

class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self.hash_function(key)
        start_idx = idx
        while self.table[idx] is not None and self.table[idx][0] != key:
            idx = (idx + 1) % self.size
            if idx == start_idx:
                raise Exception("Hash Table is full!")

        self.table[idx] = (key, value)

    def get(self, key):
        idx = self.hash_function(key)
        start_idx = idx
        while self.table[idx]:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return None

    def delete(self, key):
        idx = self.hash_function(key)
        start_idx = idx
        while self.table[idx]:
            if self.table[idx][0] == key:
                self.table[idx] = None
                return
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break

    def display(self):
        for idx, item in enumerate(self.table):
            print(f"Index {idx}: {item}")

# test cases of both implementations
# Chaining Test
print("Chaining Hash Table:")
ht_chain = HashTableChaining(10)
ht_chain.insert("apple", 1)
ht_chain.insert("banana", 2)
ht_chain.insert("grape", 3)
ht_chain.display()
print("Get 'banana':", ht_chain.get("banana"))
ht_chain.delete("banana")
ht_chain.display()

# Linear Probing Test
print("\nLinear Probing Hash Table:")
ht_linear = HashTableLinearProbing(10)
ht_linear.insert("apple", 1)
ht_linear.insert("banana", 2)
ht_linear.insert("grape", 3)
ht_linear.display()
print("Get 'grape':", ht_linear.get("grape"))
ht_linear.delete("banana")
ht_linear.display()
