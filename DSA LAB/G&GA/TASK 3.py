import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            if neighbor in visited:
                continue
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances

# Test Case
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

print(dijkstra(graph, 'A'))
