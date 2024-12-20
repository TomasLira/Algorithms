import heapq
from collections import deque
from sys import maxsize

def cheapest_path_with_distance_constraint(n: int, edges: list[tuple[int, int, int]], path: list[int], threshold_dist: int) -> int:
    graph = [[] for _ in range(n)] 
    inverted_graph = [[] for _ in range(n)]
    
    for u,v,w in edges:
        graph[u].append((v,w))
        inverted_graph[v].append((u,w))
    
    def set_dijkstra():
        distances = [maxsize]*n 
        #parents = [-1]*n
        for path_v in path:
            # as if it was a starting vertex
            distances[path_v] = 0
        min_heap = [(0, v) for v in path]
        heapq.heapify(min_heap)
        
        while min_heap:
            current_dist,vertex = heapq.heappop(min_heap)
            if current_dist > distances[vertex]:
                continue
            for adj_v,adj_weight in inverted_graph[vertex]:
                new_distance = distances[vertex] + adj_weight
                if new_distance < distances[adj_v]:
                    distances[adj_v] = new_distance
                    #parents[adj_v] = vertex
                    heapq.heappush(min_heap,(distances[adj_v],adj_v))    
        return distances
                   
    path_distances = set_dijkstra()              
    #print(path_distances)
    
    def dijkstra(src:int,dst:int)->list[int]:
        distances = [maxsize]*n
        distances[src] = 0
        parents = [-1]*n
        min_heap = [(0,src)]
        
        while min_heap:
            current_dist,vertex = heapq.heappop(min_heap)
            if current_dist > distances[vertex]:
                continue
            if vertex == dst:
                return parents,distances[vertex]
            for adj_v,adj_weight in graph[vertex]:
                new_distance = adj_weight + distances[vertex]
                if new_distance < distances[adj_v] and path_distances[adj_v] < threshold_dist:
                    distances[adj_v] = new_distance
                    parents[adj_v] = vertex
                    heapq.heappush(min_heap,(adj_weight,adj_v))
        return []
    
    return dijkstra(path[0],path[-1])
        
n = 5
edges = [
    (0, 1, 2),
    (1, 2, 4),
    (2, 3, 1),
    (0, 3, 8),
    (3, 4, 3)
]
path = [0, 2, 4]
threshold_dist = 5

print(cheapest_path_with_distance_constraint(n, edges, path, threshold_dist))


# Time complexity is unknown
def cheapest_path_with_distance_constraint(n: int, edges: list[tuple[int, int, int]], path: list[int], threshold_dist: int) -> int:
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((weight, v)) 
    
    distances_to_path = [maxsize] * n
    
    def bfs_from_path_nodes():
        queue = deque([(0, v) for v in path]) 
        for _, v in queue:
            distances_to_path[v] = 0
        while queue:
            current_distance, vertex = queue.popleft()
            if current_distance >= threshold_dist:
                continue
            for weight, adj_v in graph[vertex]:
                adj_distance = current_distance + weight
                if adj_distance < distances_to_path[adj_v]:
                    distances_to_path[adj_v] = adj_distance
                    queue.append((adj_distance, adj_v))
    bfs_from_path_nodes() 

    def dijkstra_with_constraint(src, end):
        distances = [maxsize] * n
        distances[src] = 0
        min_heap = [(0, src)]
        
        while min_heap:
            current_distance, vertex = heapq.heappop(min_heap)
            if vertex == end:
                return distances[vertex]
            
            for adj_w, adj_v in graph[vertex]:
                adj_distance = current_distance + adj_w
                if adj_distance < distances[adj_v] and distances_to_path[adj_v] <= threshold_dist:
                    distances[adj_v] = adj_distance
                    heapq.heappush(min_heap, (adj_distance, adj_v))
        
        return -1 
    start, end = path[0], path[-1]
    return dijkstra_with_constraint(start, end)

n = 5
edges = [
    (0, 1, 2),
    (1, 2, 4),
    (2, 3, 1),
    (0, 3, 8),
    (3, 4, 3)
]
path = [0, 2, 4]
threshold_dist = 5

print(cheapest_path_with_distance_constraint(n, edges, path, threshold_dist))
