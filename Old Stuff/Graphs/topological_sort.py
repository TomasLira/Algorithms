def topological_sort(n: int, edges: list[list[int]]):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    sorted_vertices = []
    visited = set()
    rec_stack = set()
    
    def dfs(vertex):
        visited.add(vertex) 
        rec_stack.add(vertex)
        for adj_v in graph[vertex]:
            if adj_v not in visited:
                dfs(adj_v)
            if adj_v in rec_stack:
                print("Back Edge detected! NOT DAG")
        sorted_vertices.append(vertex)  
        rec_stack.remove(vertex)

    for vertex in range(n):
        if vertex not in visited:
            dfs(vertex)
        print(visited)
    return sorted_vertices[::-1]


n = 6
edges = [
    [2,3],
    [5,2],
    [3,1],
    [4,1],
    [4,0],
    [5,0]
]

topological_order = topological_sort(n, edges)
print("Topological Order:", topological_order)

