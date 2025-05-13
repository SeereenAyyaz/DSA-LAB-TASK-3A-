class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}
        self.vertices = set()

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            self.adj_list[from_vertex].append(to_vertex)
            if not self.directed:
                self.adj_list[to_vertex].append(from_vertex)

    def display_adj_list(self):
        print("Adjacency List:", self.adj_list)

    def display_adj_matrix(self):
        matrix = {v: {u: 0 for u in self.vertices} for v in self.vertices}
        for v in self.adj_list:
            for neighbor in self.adj_list[v]:
                matrix[v][neighbor] = 1
        print("Adjacency Matrix:")
        print(" ", " ".join(self.vertices))
        for v in self.vertices:
            print(v, " ".join(str(matrix[v][u]) for u in self.vertices))
# Test Case
g = Graph(directed=True)
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.display_adj_list()
g.display_adj_matrix()
