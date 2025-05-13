class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full!")
            return
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = element
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:  
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed

    def front_element(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def rear_element(self):
        if self.is_empty():
            return None
        return self.queue[self.rear]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        i = self.front
        elements = []
        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("Queue elements:", elements)

# test cases
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()

cq.dequeue()
cq.enqueue(60)
cq.display()

print("Front Element:", cq.front_element()) 
print("Rear Element:", cq.rear_element())    

