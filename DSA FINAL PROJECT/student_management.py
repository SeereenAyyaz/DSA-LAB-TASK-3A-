from colorama import Fore, Style

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    def is_empty(self):
        return len(self.stack) == 0
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    def is_empty(self):
        return len(self.queue) == 0
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

def linear_search(students, target):
    for student in students:
        if student['name'].lower() == target.lower():
            return student
    return None

def bubble_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if students[j]['name'].lower() > students[j+1]['name'].lower():
                students[j], students[j+1] = students[j+1], students[j]

def preload_students():
    return [
        {'name': 'Aria', 'course': 'Science'},
        {'name': 'Ross', 'course': 'Math'},
        {'name': 'Luna', 'course': 'History'},
        {'name': 'Mason', 'course': 'Physics'},
        {'name': 'Ella', 'course': 'Biology'},
        {'name': 'Noah', 'course': 'Chemistry'},
        {'name': 'Olivia', 'course': 'English'},
        {'name': 'Liam', 'course': 'Computer Science'},
        {'name': 'Sophia', 'course': 'Economics'},
        {'name': 'James', 'course': 'Business'},
        {'name': 'Amelia', 'course': 'Art'},
        {'name': 'Benjamin', 'course': 'Engineering'},
        {'name': 'Charlotte', 'course': 'Political Science'},
        {'name': 'Lucas', 'course': 'Statistics'},
        {'name': 'Mila', 'course': 'Philosophy'}
    ]
def main():
    students = preload_students()
    stack = Stack()
    queue = Queue()

    for student in students:
        stack.push(student['name'])
        queue.enqueue(student['name'])

    while True:
        print(Fore.YELLOW + "\n=== Menu ===" + Style.RESET_ALL)
        print("1. Add Student")
        print("2. Search Student (Linear Search)")
        print("3. Display Students (Sorted by Name)")
        print("4. Stack Operations")
        print("5. Queue Operations")
        print("6. Exit")

        choice = input(Fore.CYAN + "\nEnter your choice (1-6): " + Style.RESET_ALL)

        if choice == '1':
            name = input("Enter student's name: ")
            course = input("Enter student's course: ")
            students.append({'name': name, 'course': course})
            stack.push(name)
            queue.enqueue(name)
            print(Fore.GREEN + "Student added successfully!" + Style.RESET_ALL)

        elif choice == '2':
            search_name = input("Enter name to search: ")
            result = linear_search(students, search_name)
            if result:
                print(Fore.GREEN + f"Student found: Name: {result['name']}, Course: {result['course']}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Student not found." + Style.RESET_ALL)

        elif choice == '3':
            if not students:
                print(Fore.RED + "No students to display." + Style.RESET_ALL)
            else:
                bubble_sort(students)
                print(Fore.YELLOW + "\n=== Students (Sorted) ===" + Style.RESET_ALL)
                for student in students:
                    print(Fore.CYAN + f"Name: {student['name']}, Course: {student['course']}" + Style.RESET_ALL)

        elif choice == '4':
            if stack.is_empty():
                print(Fore.RED + "Stack is empty." + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "\n=== Stack Operations ===" + Style.RESET_ALL)
                print(Fore.CYAN + f"Top Student in Stack: {stack.peek()}" + Style.RESET_ALL)
                popped_student = stack.pop()
                print(Fore.CYAN + f"Popped Student from Stack: {popped_student}" + Style.RESET_ALL)

        elif choice == '5':
            if queue.is_empty():
                print(Fore.RED + "Queue is empty." + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "\n=== Queue Operations ===" + Style.RESET_ALL)
                print(Fore.CYAN + f"Front Student in Queue: {queue.front()}" + Style.RESET_ALL)
                dequeued_student = queue.dequeue()
                print(Fore.CYAN + f"Dequeued Student from Queue: {dequeued_student}" + Style.RESET_ALL)

        elif choice == '6':
            print(Fore.GREEN + "Exiting program. Goodbye!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Please select from 1-6." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

