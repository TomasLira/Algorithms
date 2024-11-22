from typing import List
import heapq
from collections import deque
from sys import maxsize

# Using Queue
def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = [[] for _ in range(n)]
    for u, v, weight in flights:
        graph[u].append((v, weight))
        
    queue = deque([(0, src, 0)])  # (step, vertex,current weight distance): step: num of vertices till src
    distance = [maxsize] * n
    distance[src] = 0
        
    # we are updating based of layers (queue)
    while queue:
        step, vertex, current_distance = queue.popleft()
        if step > k:
            continue
            
        for adj_v, adj_weight in graph[vertex]:
            if current_distance + adj_weight < distance[adj_v]:
                distance[adj_v] = current_distance + adj_weight
                queue.append((step + 1, adj_v, distance[adj_v]))
            
    return distance[dst] if distance[dst] != maxsize else -1

# Bellman-Ford
# Can use restrictions, in this case we are only allowed to make k+1 relaxations
def findCheapestPriceBellmanFord(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    distance = [maxsize] * n
    distance[src] = 0

    for _ in range(k + 1):
        distance_temp = distance.copy()
        for u, v, weight in flights:
            if distance[u] != maxsize and distance[u] + weight < distance_temp[v]:
                distance_temp[v] = distance[u] + weight
        distance = distance_temp
    
    return distance[dst] if distance[dst] != maxsize else -1
