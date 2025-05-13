class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            return False
        return True

def detect_cycle_undirected(graph):
    nodes = list(graph.keys())
    node_to_index = {node: i for i, node in enumerate(nodes)}
    uf = UnionFind(len(nodes))
    
    for node in graph:
        for neighbor in graph[node]:
            if uf.union(node_to_index[node], node_to_index[neighbor]):
                return True 
    return False 

def detect_cycle_directed(graph):
    visited = set()
    recursion_stack = set()
    
    def dfs(node):
        if node in recursion_stack:
            return True
        if node in visited:
            return False
        
        visited.add(node)
        recursion_stack.add(node)
        
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        recursion_stack.remove(node)
        return False
    for node in graph:
        if dfs(node):
            return True
    return False  
