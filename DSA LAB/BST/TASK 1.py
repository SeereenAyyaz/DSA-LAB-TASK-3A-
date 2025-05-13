class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left:
                self._insert(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert(current.right, value)
            else:
                current.right = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if not current:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, current, value):
        if not current:
            return current
        if value < current.value:
            current.left = self._delete(current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:
            if not current.left:
                return current.right
            elif not current.right:
                return current.left
            temp_val = self._min_value_node(current.right)
            current.value = temp_val.value
            current.right = self._delete(current.right, temp_val.value)
        return current

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, current):
        if current:
            self._inorder_traversal(current.left)
            print(current.value, end=" ")
            self._inorder_traversal(current.right)

# test cases
# Creating BST
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]
for val in values:
    bst.insert(val)
bst.inorder_traversal()  
print(bst.search(60))  
print(bst.search(100))
bst.delete(20)   
bst.inorder_traversal()  
bst.delete(30)  
bst.inorder_traversal() 
bst.delete(50)  
bst.inorder_traversal()  
