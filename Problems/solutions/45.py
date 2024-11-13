from collections import deque

def specified_path(n: int, edges: list[list[int]], L: list[int]):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    
    parents = [-1] * n  
    visited = [False] * n
    
    for vertex in L:
        visited[vertex] = True
    
    def bfs(src: int, target: int, visited_local: list[bool]):
        queue = deque([src])
        
        while queue:
            v = queue.popleft()
            for adj in graph[v]:
                if not visited_local[adj]:
                    queue.append(adj)
                    visited_local[adj] = True
                    parents[adj] = v
                    if adj == target:
                        return 

    for i in range(len(L) - 1):
        src, target = L[i], L[i + 1]
        
        visited[target] = False
        visited_copy = visited.copy()
        
        bfs(src, target, visited_copy)        
        visited[target] = True

    return parents



n = 5
edges = [
    [0, 1],
    [1, 2],
    [2, 0],  
    [1, 3],
    [3, 4],
    [4, 1]  
]

L = [0, 3, 4]

parents = specified_path(n, edges, L)
print("Parent Array:", parents)

def reconstruct_path(L, parents):
    path = []
    
    for i in range(len(L) - 1):
        src, target = L[i], L[i + 1]
        segment = []
        current = target
        
        while current != -1 and current != src:
            segment.append(current)
            current = parents[current]        
        segment.append(src)
        path.extend(reversed(segment) if not path else reversed(segment[:-1]))
    
    return path

print("Specified Path of L:", reconstruct_path(L, parents))
