# Stack Using Arrays
class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

#  Stack Using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

# test cases for both stacks 
# Testing StackArray
print("Testing Stack with Array:")
stack_array = StackArray()
stack_array.push(10)
stack_array.push(20)
stack_array.push(30)
print("Top element:", stack_array.peek())   
print("Stack size:", stack_array.size())     
print("Pop element:", stack_array.pop())     
print("Top element after pop:", stack_array.peek())  
print("Is stack empty?", stack_array.is_empty())     
print()

# Testing StackLinkedList
print("Testing Stack with Linked List:")
stack_linked = StackLinkedList()
stack_linked.push(10)
stack_linked.push(20)
stack_linked.push(30)
print("Top element:", stack_linked.peek())   
print("Stack size:", stack_linked.size())     
print("Pop element:", stack_linked.pop())     
print("Top element after pop:", stack_linked.peek())  
print("Is stack empty?", stack_linked.is_empty())     
