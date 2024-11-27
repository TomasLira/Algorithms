from collections import deque
from sys import maxsize
import heapq

def biggest_edge_cost(n:int,edges: list[tuple[int,int,int]]):
    graph = [[] for _ in range(n)]
    for u,v,w in edges:
        graph[u].append((v,w))
    
    def prim(src):
        visited = [False]*n
        min_heap = [(0,src,-1)]
        mst_edges = []
        mst_cost = 0
        
        while min_heap:
            current_weight,vertex,parent = heapq.heappop(min_heap)
            if visited[vertex]:
                continue
            visited[vertex] = True
            mst_cost += current_weight

            if parent != -1:
                mst_edges.append((parent,vertex,current_weight))
                
            for adj_v,adj_weight in graph[vertex]:
                if not visited[adj_v]:
                    heapq.heappush(min_heap,(adj_weight,adj_v,vertex))
        return mst_cost,mst_edges    
    
    cost,edges = prim(0)
    print(cost,edges)
    for v,u,u_w in edges:
        graph[v].remove((u,u_w))
        new_cost,new_edges= prim(0)
        new_cost = max(new_cost,cost)
        if new_cost != cost:
            cost = new_cost
            removed_edge = (v,u)
            edges = new_edges
        graph[v].append((u,u_w))
    return cost,edges,removed_edge,
        
n = 4
edges = [
    (0, 1, 1),
    (1, 2, 2),
    (0, 2, 2),
    (2, 3, 1),
    (1, 3, 3)
]
print(biggest_edge_cost(n, edges))