from collections import deque
from sys import maxsize

# Kahn’s algorithm
def check_dag(n: int, edges: list[tuple[int, int, int]]):
    graph = [[] for _ in range(n)]
    in_degree = [0] * n 
    for u, v, _ in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topological_order = []

    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topological_order) != n:
        return False, []
    return True, topological_order

# using dfs
def check_dag(n: int, edges: list[tuple[int, int, int]]):
    graph = [[] for _ in range(n)]
    for u, v, _ in edges:
        graph[u].append(v)

    visited = [False] * n
    rec_stack = [False] * n
    topological_order = []

    def dfs(vertex):
        visited[vertex] = True
        rec_stack[vertex] = True

        for adj in graph[vertex]:
            if not visited[adj]:
                if not dfs(adj):  
                    return False
            elif rec_stack[adj]:  
                return False

        rec_stack[vertex] = False 
        topological_order.append(vertex)  
        return True

    for i in range(n):
        if not visited[i]:
            if not dfs(i):
                return False, []  

    return True, topological_order[::-1]  

def paths(n: int, src: int, edges: list[tuple[int, int, int]], find_longest=False):
    is_dag, topological_order = check_dag(n, edges)
    if not is_dag:
        return False, "Graph is not a DAG"

    distances = [-maxsize if find_longest else maxsize] * n
    distances[src] = 0

    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))

    for node in topological_order:
        for neighbor, weight in graph[node]:
            if find_longest:
                distances[neighbor] = max(distances[neighbor], distances[node] + weight)
            else:
                distances[neighbor] = min(distances[neighbor], distances[node] + weight)
    return distances

n = 6
edges = [
    (0, 1, 5), 
    (0, 2, 3), 
    (1, 3, 6), 
    (1, 2, 2), 
    (2, 4, 4), 
    (2, 5, 2), 
    (2, 3, 7), 
    (3, 5, 1), 
    (3, 4, -1), 
    (4, 5, -2)
]

print("Shortest Path:", paths(n, 0, edges, find_longest=False))
print("Longest Path:", paths(n, 0, edges, find_longest=True))
