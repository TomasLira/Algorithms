import heapq

def prim(n: int, edges: list[tuple[int, int, int]]) -> tuple[int, list[tuple[int, int, int]]]:
    # Create an adjacency list for the graph
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    
    visited = [False] * n 
    min_heap = [(0, 0, -1)]  # (weight, vertex, parent)
    mst_cost = 0
    mst_edges = [] 
    
    while min_heap:
        weight, vertex, parent = heapq.heappop(min_heap)
        
        if visited[vertex]:
            continue
        visited[vertex] = True
        mst_cost += weight
        
        if parent != -1:
            mst_edges.append((parent, vertex, weight))
        
        for adj_v, next_weight in graph[vertex]:
            if not visited[adj_v]:
                heapq.heappush(min_heap, (next_weight, adj_v, vertex))
    
    if all(visited):
        return mst_cost, mst_edges
    else:
        return float('inf'), []  

n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst_cost, mst_edges = prim(n, edges)
print("Total cost of MST:", mst_cost)
print("Edges in MST:", mst_edges)
