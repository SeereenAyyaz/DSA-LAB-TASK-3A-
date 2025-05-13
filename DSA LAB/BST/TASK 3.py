def is_balanced(root):
    def check_balance(node):
        if not node:
            return 0, True
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        balanced = (left_balanced and right_balanced and abs(left_height - right_height) <= 1)
        return max(left_height, right_height) + 1, balanced

    _, result = check_balance(root)
    return result

# test cases
# Balanced Tree
balanced_bst = BinarySearchTree()
for val in [10, 5, 15, 2, 7, 12, 20]:
    balanced_bst.insert(val)
print(is_balanced(balanced_bst.root))  
unbalanced_bst = BinarySearchTree()
for val in [10, 5, 2]:
    unbalanced_bst.insert(val)
print(is_balanced(unbalanced_bst.root))  
