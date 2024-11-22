from collections import deque
def check_coloring(n: int, edges: list[list[int]]):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)    
    
    colors = [-1] * n
    
    def bfs(vertex):
        queue = deque([vertex])
        colors[vertex] = 0
        
        while queue:
            current = queue.popleft()
            current_color = colors[current]
            for adj_v in graph[current]:
                if colors[adj_v] == -1:
                    colors[adj_v] = 1 - current_color
                    queue.append(adj_v)
                elif colors[adj_v] == current_color:
                    return False
        return True    

    for i in range(n):
        if colors[i] == -1:
            if not bfs(i):
                return False
    return True