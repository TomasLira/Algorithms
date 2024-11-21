def check_tree(n: int, edges: list[tuple[int, int]]):
    
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n

    def dfs(vertex, parent):
        
        # this conditional wont be necessary, if repetition of vertex then backedge
        # if visited[vertex]:
        #     return True
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
    if not all(visited):
        return False
    
    return True

print(check_tree(3, [(0, 1), (1, 2)]))  # Should return True (Tree)
print(check_tree(4, [(0, 1), (1, 2), (2, 3)]))  # Should return True (Tree)
print(check_tree(4, [(0, 1), (1, 2), (2, 0)]))  # Should return False (Cycle)
print(check_tree(4, [(0, 1), (1, 2)]))  # Should return False (Disconnected)
