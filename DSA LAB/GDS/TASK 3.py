import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        self.adj_list[from_vertex].append((to_vertex, weight))

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# test cases of Dijkstra's algorithm
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 1)
g.add_edge("C", "B", 2)
g.add_edge("B", "D", 1)

print(g.dijkstra("A"))
