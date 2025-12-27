from sys import maxsize

def longest_path(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * n
    rec_stack = [False] * n
    sorted_vertices = []

    def topological(vertex):
        visited[vertex] = True
        rec_stack[vertex] = True
        for adj_v in graph[vertex]:
            if not visited[adj_v]:
                if not topological(adj_v):
                    return False
            elif rec_stack[adj_v]:
                return False
        sorted_vertices.append(vertex)
        rec_stack[vertex] = False
        return True

    for i in range(n):
        if not visited[i]:
            if not topological(i):
                return -1

    sorted_vertices.reverse() 
    
    distances = [-maxsize] * n
    distances[sorted_vertices[0]] = 0 
    
    for u in sorted_vertices:
        for v in graph[u]:
            # base case happens at first iteration!
            # top down 
            distances[v] = max(distances[v], distances[u] + 1)
    return max(distances)