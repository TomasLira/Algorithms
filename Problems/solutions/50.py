def connected_components(n:int, edges: list[tuple[int, int]]):        
    # Checks if graph is weakly connected.
    def check_weak(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [False] * n

        def dfs(vertex):
            if visited[vertex]:
                return
            visited[vertex] = True  
            for adj_v in graph[vertex]:
                if not visited[adj_v]:
                    dfs(adj_v)
        dfs(0)
        return all(visited)
    is_weak = check_weak(n,edges)
    
    # bridge is an edge that, when removed, increases the numvber of connected components in graph
    # Tarjan's algorithm
    def find_weak_bridges(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        discovery = [-1]*n
        low = [-1]*n
        parents = [-1]*n
        bridges = []
        time = [0]
        
        def dfs(vertex):
            # ideia is that low will be discovery of back edge of src vertex
            discovery[vertex] = low[vertex] = time[0]
            time[0] += 1
            for adj_v in graph[vertex]:
                if discovery[adj_v] == -1:
                    parents[adj_v] = vertex
                    dfs(adj_v)
                    low[vertex] = min(low[vertex], low[adj_v])
                    # low[adj_v] gets the earliest discovery from back edge
                    if discovery[vertex] < low[adj_v]:
                        bridges.append((adj_v,vertex))
                # back edge detected vertex-adj_v, update low getting discovery of adj_v
                elif adj_v != parents[vertex]:
                    low[vertex] = min(low[vertex], discovery[adj_v])                            
                    
        for i in range(n):
            if discovery[i] == -1:
                dfs(i)
        return bridges

    print("Is graph weakly connected:", is_weak)
    print("Bridges in the graph:", find_weak_bridges(n, edges))
    
    
    def find_scc(n, edges):
        ...


n1 = 3
edges1 = [(0, 1), (1, 2), (2, 0)]
connected_components(n1, edges1)

n2 = 4
edges2 = [(0, 1), (1, 2), (2, 3)]
connected_components(n2, edges2)
                    