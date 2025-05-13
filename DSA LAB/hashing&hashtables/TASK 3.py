class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        # Always add node right after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # Remove an existing node
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return None
        self._move_to_front(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self._move_to_front(node)

    def display(self):
        current = self.head.next
        result = {}
        while current != self.tail:
            result[current.key] = current.value
            current = current.next
        print("Cache State:", result)

# test cases
cache = LRUCache(5)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.put(4, "D")
cache.put(5, "E")
cache.display()

cache.get(2) 
cache.put(6, "F")  
cache.display()

cache.get(3)
cache.put(7, "G") 
cache.display()
