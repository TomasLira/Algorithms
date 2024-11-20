import heapq
from typing import List

# O(n^2 log(n)) graph is complete
def minCostConnectPoints(points: List[List[int]]) -> int:
        n = len(points)        
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                graph[i].append((j, dist)) 
                graph[j].append((i, dist))  
        
        visited = [False] * n
        min_heap = [(0, 0)]  
        min_cost = 0 
        
        while min_heap:
            cost, v = heapq.heappop(min_heap)
            
            if visited[v]:  
                continue
            
            visited[v] = True 
            min_cost += cost 
            
            for adj_v, adj_cost in graph[v]:
                if not visited[adj_v]:
                    heapq.heappush(min_heap, (adj_cost, adj_v))      
        return min_cost