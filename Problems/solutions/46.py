import heapq
from sys import maxsize

# Alter to V^2
def find_min_max_distance(n: int, edges: list[tuple[int, int, int]], L: list[int]) -> int:
    adjacency_list = [[] for _ in range(n)]
    for src, dest, weight in edges:
        adjacency_list[src].append((dest, weight))
    
    def dijkstra(source: int):
        distances = [maxsize] * n
        distances[source] = 0
        
        min_heap = [(0, source)] 
        
        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in adjacency_list[current_vertex]:
                distance_to_neighbor = current_distance + weight
                if distance_to_neighbor < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor
                    heapq.heappush(min_heap, (distance_to_neighbor, neighbor))
        
        max_distance = max(distances)
        max_distance_vertex = distances.index(max_distance)
        return max_distance, max_distance_vertex
    
    min_of_max_distances = maxsize
    best_vertex = -1
    
    for start_vertex in L:
        max_distance, farthest_vertex = dijkstra(start_vertex)
        if max_distance < min_of_max_distances:
            min_of_max_distances = max_distance
            best_vertex = farthest_vertex
    
    return best_vertex

num_vertices = 5
edges = [
    (0, 1, 10),
    (1, 2, 20),
    (2, 3, 5),
    (3, 4, 15)
]
start_vertices = [0, 2, 4]

result = find_min_max_distance(num_vertices, edges, start_vertices)
print("Best vertex with minimum max distance:", result)
