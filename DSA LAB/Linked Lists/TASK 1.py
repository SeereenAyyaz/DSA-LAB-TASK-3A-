class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if not current:
            print("Position out of bounds")
            return

        new_node.next = current.next
        current.next = new_node
    def delete_by_value(self, value):
        current = self.head

        if not current:
            print("List is empty")
            return

        if current.data == value:
            self.head = current.next
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if not current:
            print(f"Value {value} not found in list")
            return

        prev.next = current.next
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1  
    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return

        while current:
            print(current.data, end=" → " if current.next else "")
            current = current.next
        print()

# test cases
ll = SinglyLinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
print("Initial list:")
ll.display()
ll.insert_at_end(5)
print("\nAfter inserting 5 at end:")
ll.display()
ll.delete_by_value(3)
print("\nAfter deleting 3:")
ll.display()
position = ll.search(4)
if position != -1:
    print(f"\nElement 4 found at position {position}")
else:
    print("\nElement 4 not found")
ll.insert_at_beginning(0)
print("\nAfter inserting 0 at beginning:")
ll.display()
ll.insert_at_position(9, 3)
print("\nAfter inserting 9 at position 3:")
ll.display()
