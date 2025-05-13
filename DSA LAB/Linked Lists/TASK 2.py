class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def create_loop(self, pos):
        if pos == -1:
            return
        loop_start = None
        current = self.head
        count = 0
        last_node = None
        while current:
            if count == pos:
                loop_start = current
            last_node = current
            current = current.next
            count += 1
        if last_node:
            last_node.next = loop_start
    def detect_loop(self):
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print(f"Loop detected at node with value {slow.data}")
                return slow  
        print("No loop detected")
        return None  
    def find_loop_start(self):
        intersection = self.detect_loop()
        if not intersection:
            return None

        ptr1 = self.head
        ptr2 = intersection

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        print(f"Start of loop is at node with value {ptr1.data}")
        return ptr1
    def remove_loop(self):
        start_node = self.find_loop_start()
        if not start_node:
            return  
        temp = start_node
        while temp.next != start_node:
            temp = temp.next
        temp.next = None
        print("Loop removed successfully")
    def display(self):
        current = self.head
        visited = set()
        while current:
            if current in visited:
                print(f"({current.data}) -> Loop back detected, stopping display.")
                break
            print(current.data, end=" → " if current.next else "")
            visited.add(current)
            current = current.next
        print()

# test cases
ll = SinglyLinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.create_loop(2)
ll.detect_loop()
ll.remove_loop()
print("\nLinked List after removing loop:")
ll.display()
