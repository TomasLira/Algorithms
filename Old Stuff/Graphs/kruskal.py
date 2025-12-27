import matplotlib.pyplot as plt
import networkx as nx
import heapq

n = 5 
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = n
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            self.size -= 1
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(n, edges):
    uf = UF(n)
    min_heap = []
    for u, v, weight in edges:
        heapq.heappush(min_heap, (weight, u, v))
    
    mst_weight = 0
    mst_edges = []
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            mst_weight += weight
    return mst_weight, mst_edges

mst_weight, mst_edges = kruskal(n, edges)

G = nx.Graph()
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
edge_labels = {(u, v): f"{w}" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Original Graph")

mst_G = nx.Graph()
mst_G.add_weighted_edges_from(mst_edges)

plt.subplot(1, 2, 2)
nx.draw(mst_G, pos, with_labels=True, node_color="lightgreen", edge_color="orange", node_size=500, font_size=10)
mst_edge_labels = {(u, v): f"{w}" for u, v, w in mst_edges}
nx.draw_networkx_edge_labels(mst_G, pos, edge_labels=mst_edge_labels)
plt.title(f"MST (Weight: {mst_weight})")

plt.show()
