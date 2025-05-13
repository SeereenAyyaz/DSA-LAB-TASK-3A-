class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size 

   
    def hash_function(self, key):
        return hash(key) % self.size

    
    def insert_chaining(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]  
        else:
           
            self.table[index].append((key, value))

    def get_chaining(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]  
        return None  

    def delete_chaining(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    del self.table[index][i] 
                    return True
        return False

    
    def insert_linear_probing(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:  
            if self.table[index][0] == key:
                self.table[index] = (key, value)  
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value) 

    def get_linear_probing(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1] 
            index = (index + 1) % self.size
            if index == original_index:
                break  
        return None  

    def delete_linear_probing(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break          return False  

# Test cases
ht = HashTable(10)
ht.insert_chaining("name", "Alice")
ht.insert_chaining("age", 25)
print(ht.get_chaining("name"))  
ht.delete_chaining("age")
print(ht.get_chaining("age")) 

ht2 = HashTable(10)
ht2.insert_linear_probing("name", "Alice")
ht2.insert_linear_probing("age", 25)
print(ht2.get_linear_probing("name"))  
ht2.delete_linear_probing("age")
print(ht2.get_linear_probing("age"))  
