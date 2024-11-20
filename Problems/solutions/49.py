def findCircleNum(isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(vertex):
            if visited[vertex]:
                return
            visited[vertex] = True
            for adj_v in range(n):
                if isConnected[vertex][adj_v] == 1 and not visited[adj_v]:
                    dfs(adj_v)
        provinces = 0        
        
        for vertex in range(n):
            if not visited[vertex]:
                provinces += 1
                dfs(vertex)
        
        return provinces



def findCircleNum(isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)
        
        visited = [False] * n
        
        def dfs(vertex):
            if visited[vertex]:
                return
            visited[vertex] = True
            for adj_v in graph[vertex]:
                dfs(adj_v)
        
        provinces = 0
        
        for vertex in range(n):
            if not visited[vertex]:
                provinces += 1
                dfs(vertex)
        
        return provinces
