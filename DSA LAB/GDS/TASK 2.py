from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        self.adj_list[from_vertex].append(to_vertex)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.adj_list[vertex])
        return result

    def dfs(self, start):
        visited = set()
        result = []
        self._dfs_recursive(start, visited, result)
        return result

    def _dfs_recursive(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)

# test cases of BFS and DFS
g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print(g.bfs(0))  
print(g.dfs(0))  
