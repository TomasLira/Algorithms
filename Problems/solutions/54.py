from collections import deque
import heapq
from sys import maxsize
# Implementação do primeiro esta errado

def biggest_edge_cost(n: int, edges: list[tuple[int, int, int]]):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w)) 

    def prim(src):
        visited = [False] * n
        min_heap = [(0, src, -1)] 
        mst_edges = []
        mst_cost = 0

        while min_heap:
            current_weight, vertex, parent = heapq.heappop(min_heap)
            if visited[vertex]:
                continue
            visited[vertex] = True
            mst_cost += current_weight

            if parent != -1:
                mst_edges.append((parent, vertex, current_weight))

            for adj_v, adj_weight in graph[vertex]:
                if not visited[adj_v]:
                    heapq.heappush(min_heap, (adj_weight, adj_v, vertex))
        return mst_cost, mst_edges

    original_cost, original_edges = prim(0)
    print(original_edges)
    
    min_weights = [(maxsize, None) for _ in range(len(original_edges))]
    side_1 = set()
    idx = 0
    for u, v, w in original_edges:
        if u not in side_1:
            side_1.add(u)
        for new_u in side_1:
            for adj_vertex, weight in graph[new_u]:
                if adj_vertex not in side_1 and (adj_vertex,weight) != (v,w):
                    diff = weight - w
                    if diff < min_weights[idx][0]:
                        min_weights[idx] = (diff, (u, v, w))
        idx += 1

    max_edge = max((edge for edge in min_weights if edge[0] != maxsize), key=lambda x: x[0])
    return max_edge[1], original_cost + max_edge[0]

def biggest_edge_cost(n: int, edges: list[tuple[int, int, int]]):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def prim(src):
        visited = [False] * n
        min_heap = [(0, src, -1)]
        mst_edges = []
        mst_cost = 0

        while min_heap:
            current_weight, vertex, parent = heapq.heappop(min_heap)
            if visited[vertex]:
                continue
            visited[vertex] = True
            mst_cost += current_weight
            if parent != -1:
                mst_edges.append((parent, vertex, current_weight))

            for adj_v, adj_weight in graph[vertex]:
                if not visited[adj_v]:
                    heapq.heappush(min_heap, (adj_weight, adj_v, vertex))
        return mst_cost, mst_edges
    
    initial_cost, mst_edges = prim(0)

    max_cost = initial_cost
    critical_edge = None

    for v, u, weight in mst_edges:
        graph[v].remove((u, weight))
        graph[u].remove((v, weight))
        
        new_cost, _ = prim(0)
        
        if new_cost > max_cost:
            max_cost = new_cost
            critical_edge = (v, u, weight)
        
        graph[v].append((u, weight))
        graph[u].append((v, weight))
    
    return max_cost, critical_edge