from sys import maxsize

def bellman_ford(n: int, edges: list[list[int]], src: int):
    dist = [maxsize] * n
    dist[src] = 0

    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != maxsize and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
        
    for u, v, weight in edges:
        if dist[u] != maxsize and dist[u] + weight < dist[v]:
            print("Graph has negative weight cycle")
            return None

    return dist

edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

n = 5  
src = 0
distances = bellman_ford(n, edges, src)
if distances:
    print(f" {src}: {distances}")
