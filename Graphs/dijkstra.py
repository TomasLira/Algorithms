import heapq

def dijkstra(n: int, edges: list[tuple[int, int, int]], start: int = 0) -> list[int]:
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    
    distances = [float('inf')] * n
    distances[start] = 0  
    min_heap = [(0, start)]  
    
    while min_heap:
        current_dist, vertex = heapq.heappop(min_heap)
        
        # A previously pushed longer distance might still be in the heap.
        if current_dist > distances[vertex]:
            continue
            
        for adj_v, weight in graph[vertex]:
            distance = current_dist + weight
            
            if distance < distances[adj_v]:
                distances[adj_v] = distance
                heapq.heappush(min_heap, (distance, adj_v))
    
    return distances 

n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

print("Shortest distances from vertex 0:", dijkstra(n, edges))
