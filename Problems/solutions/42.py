from collections import deque

def bfs(graph, node, colors):
    queue = deque([node])

    while queue:
        vertex = queue.popleft()
        color = colors[vertex]
        for neighbor in graph[vertex]:
            if colors[neighbor] == -1:
                colors[neighbor] = 1 - color
                queue.append(neighbor)
            elif colors[neighbor] == color:
                return False
    return True

def is_bipartite(graph):
    n = len(graph)
    colors = [-1] * n

    for i in range(n):
        if colors[i] == -1:
            colors[i] = 0
            if not bfs(graph, i, colors):
                return False
    return True

graph1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

graph2 = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
print(is_bipartite(graph1))  
print(is_bipartite(graph2)) 