class DynamicArray:
    def __init__(self):
        self.capacity = 2  
        self.size = 0      
        self.array = self.make_array(self.capacity)
    def make_array(self, new_capacity):
        return [None] * new_capacity
    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    def insert_end(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1
    def insert_at(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds!")
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1
    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds!")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size > 0 and self.size == self.capacity // 4:
            self.resize(self.capacity // 2)
    def search(self, element):
        for i in range(self.size):
            if self.array[i] == element:
                return i
        return -1
    def display(self):
        return [self.array[i] for i in range(self.size)]

arr = DynamicArray()
arr.insert_end(10)
arr.insert_end(20)
arr.insert_end(30)
print("After insert_end:", arr.display())  
arr.insert_at(1, 15)
print("After insert_at(1, 15):", arr.display())  
arr.delete_at(2)
print("After delete_at(2):", arr.display()) 
index = arr.search(30)
print("Search 30 found at index:", index)  
index = arr.search(100)
print("Search 100 found at index:", index) 
