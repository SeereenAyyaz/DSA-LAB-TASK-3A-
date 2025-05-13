def find_LCA(root, n1, n2):
    if not root:
        return None
    if n1 < root.value and n2 < root.value:
        return find_LCA(root.left, n1, n2)
    elif n1 > root.value and n2 > root.value:
        return find_LCA(root.right, n1, n2)
    else:
        return root

# test cases
#  BST
bst = BinarySearchTree()
for value in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(value)
lca_node = find_LCA(bst.root, 5, 15)
print(f"LCA of 5 and 15: {lca_node.value}") 
lca_node = find_LCA(bst.root, 5, 25)
print(f"LCA of 5 and 25: {lca_node.value}")  
lca_node = find_LCA(bst.root, 25, 35)
print(f"LCA of 25 and 35: {lca_node.value}")  
