class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.adj_list = {i: [] for i in range(vertices)}
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_matrix[v1][v2] = 1
        if not self.directed:
            self.adj_list[v2].append(v1)
            self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        self.adj_matrix[v1][v2] = 0
        if not self.directed:
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            self.adj_matrix[v2][v1] = 0

    def display(self):
        print("Adjacency List Representation:")
        for v in self.adj_list:
            print(f"{v}: {self.adj_list[v]}")
        
        print("\nAdjacency Matrix Representation:")
        for row in self.adj_matrix:
            print(row)

# Test Case
g = Graph(5, directed=False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.display()
