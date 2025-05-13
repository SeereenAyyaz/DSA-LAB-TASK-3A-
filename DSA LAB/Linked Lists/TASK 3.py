class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    def delete_at_position(self, position):
        if self.head is None or position < 0:
            print("Invalid position or empty list")
            return
        
        current = self.head
        count = 0

        if position == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        
        while current and count < position:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of bounds")
            return

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" → " if current.next else "")
            last = current  
            current = current.next
        print()
        return last
    def traverse_reverse(self):
        last = self.traverse_forward()
        current = last
        while current:
            print(current.data, end=" → " if current.prev else "")
            current = current.prev
        print()

# test cases
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_end(5)
print("Linked List (forward):")
dll.traverse_forward()
print("\nLinked List (reverse):")
dll.traverse_reverse()
dll.delete_at_position(2)
print("\nLinked List after deleting node at position 2 (forward):")
dll.traverse_forward()
print("\nLinked List after deleting node at position 2 (reverse):")
dll.traverse_reverse()
