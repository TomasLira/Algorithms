def criticalConnections(n:int, connections:list[list[int]]):
        graph = [[] for _ in  range(n)]
        #discovery
        disc = [-1]*n
        #depth
        low = [-1]*n
        result = []
        time = 0
        
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(vertex, parent,time):
            disc[vertex] = time
            low[vertex] = time
            time += 1
            
            for adj_v in graph[vertex]:
                if adj_v == parent:
                    continue
                if disc[adj_v] == -1:
                    dfs(adj_v,vertex,time)
                    # updates value of low[vertex]
                    # If no back edges, then low[vertex] > low[adj_v]
                    low[vertex] = min(low[vertex],low[adj_v])
                    
                    if low[adj_v] > disc[vertex]:
                        result.append([adj_v,vertex])
                else:
                    # adj_v is known, checks if they have backedges an change vertex's value
                    low[vertex] = min(low[vertex],low[adj_v])
        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1,time)
        return result
                

                
            
            