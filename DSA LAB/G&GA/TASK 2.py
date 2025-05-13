from collections import deque

class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        if not self.directed:
            self.adj_list[v2].append(v1)

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque([start])
        visited[start] = True
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        visited = [False] * self.vertices
        result = []
        
        def dfs_helper(node):
            visited[node] = True
            result.append(node)
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

# Test Case
g = Graph(6, directed=False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("BFS:", g.bfs(0))  
print("DFS:", g.dfs(0)) 

