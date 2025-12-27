def is_valid_tree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:  
        return False
    
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    
    def dfs(vertex, parent):
        visited[vertex] = True
        for adj_v in graph[vertex]:
            if not visited[adj_v]:
                if not dfs(adj_v, vertex):
                    return False
            elif adj_v != parent:
                return False
        return True
    if not dfs(0, -1):
        return False    
    
    return all(visited)
