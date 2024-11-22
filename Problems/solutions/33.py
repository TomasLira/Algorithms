class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        discovery = [-1]*n
        low = [-1]*n
        parents = [-1]*n
        bridges = []
        time = [0]
        
        def dfs(vertex):
            discovery[vertex] = low[vertex] = time[0]
            time[0] += 1
            for adj_v in graph[vertex]:
                if discovery[adj_v] == -1:
                    parents[adj_v] = vertex
                    dfs(adj_v)
                    low[vertex] = min(low[adj_v],low[vertex])
                    
                    # used to find articulation vertex so < instead of > 
                    if discovery[vertex] < low[adj_v]:
                        bridges.append((vertex,adj_v))
                
                elif parents[vertex] != adj_v:
                    # think as if the same vertex could have multiple back edges
                    low[vertex] = min(low[vertex], discovery[adj_v])
        for i in range(n):
            if discovery[i] == -1:
                dfs(i)
        return bridges