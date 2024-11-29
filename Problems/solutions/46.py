from sys import maxsize
import heapq

def find_min_max_distance(n: int, edges: list[tuple[int, int, int]], L: list[int]) -> int:
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    max_distances_L = [-maxsize] * n
    L_set = set(L)

    def dijkstra(src: int):
        distances = [maxsize] * n
        distances[src] = 0
        min_heap = [(0, src)] 

        while min_heap:
            current_distance, vertex = heapq.heappop(min_heap)

            if current_distance > distances[vertex]:
                continue

            max_distances_L[vertex] = max(max_distances_L[vertex], current_distance)

            for adj_v, adj_weight in graph[vertex]:
                new_distance = current_distance + adj_weight
                if new_distance < distances[adj_v]:
                    distances[adj_v] = new_distance
                    heapq.heappush(min_heap, (new_distance, adj_v))
    
    for vertex_l in L:
        dijkstra(vertex_l)
    
    min_dist_v = -1
    min_dist = maxsize
    for vertex, distance in enumerate(max_distances_L):
        if vertex not in L_set and distance < min_dist:
            min_dist = distance
            min_dist_v = vertex
    return min_dist_v


n = 6
edges = [
    (0, 1, 2), (1, 2, 3), (2, 3, 4),
    (3, 4, 5), (4, 5, 6), (5, 0, 1),
    (2, 0, 3), (3, 1, 2), (4, 2, 1)
]
L = [0, 2]


resultado = find_min_max_distance(n, edges, L)
print(f"O vértice com a menor maior distância dos vértices em L é: {resultado}")
