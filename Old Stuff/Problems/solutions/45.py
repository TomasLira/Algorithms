from collections import deque

def shortest_path_through_vertices(n: int, edges: list[list[int]], L: list[int]):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    
    visited_L = [False] * n
    full_path = []
    
    for l_vertex in L:
        visited_L[l_vertex] = True
    visited_L[L[0]] = False 
    
    def bfs(src: int, dst: int, visited_local: list[bool]) -> list[int]:
        queue = deque([src])
        parents = [-1] * n  
        visited_local[src] = True
        
        while queue:
            vertex = queue.popleft()
            if vertex == dst:
                break
            for adj_v in graph[vertex]:
                if not visited_local[adj_v]:
                    queue.append(adj_v)
                    visited_local[adj_v] = True
                    parents[adj_v] = vertex
        return parents

    def reconstruct_path(parents: list[int], src: int, dst: int) -> list[int]:
        path = []
        current = dst
        while current != -1:
            path.append(current)
            current = parents[current]
        if path[-1] != src:
            return []  
        path.reverse()
        return path

    for i in range(1, len(L)):
        src, dst = L[i - 1], L[i]
        #print(src,dst)
        visited_L[dst] = False 
        visited = visited_L.copy()
        parents = bfs(src, dst, visited)
        path = reconstruct_path(parents, src, dst)
        if not path:
            return []  
        if full_path and full_path[-1] == src:
            path = path[1:] 
        full_path.extend(path)
    
    return full_path


edges = [[0, 1], [1, 2], [0, 3], [3, 4], [4, 2], [2, 5],[2,1],[1,0]]
n = 6 
L= [0,2,4]

print(shortest_path_through_vertices(n,edges,L))
