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

import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(n, edges):
    G = nx.Graph()
    G.add_nodes_from(range(n))    
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)
    pos = nx.spring_layout(G, seed=42) 
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')
    edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    plt.title("Graph Visualization")
    plt.show()

n = 8
edges = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5), (0, 4, 15),
    (1, 3, 15), (1, 4, 12), (1, 5, 7), (2, 3, 4),
    (2, 5, 9), (3, 4, 8), (3, 6, 11), (4, 6, 13),
    (5, 6, 3), (5, 7, 14), (6, 7, 1)
]
mst_cost, mst_edges = prim(n, edges)
print("Total cost of MST:", mst_cost)
print("Edges in MST:", mst_edges)

visualize_graph(n, edges)

