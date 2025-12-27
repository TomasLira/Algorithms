from sys import maxsize
import heapq
import numpy as np

# Bellman ford implementation
#https://leetcode.com/problems/path-with-maximum-probability/solutions/731767/java-python-3-2-codes-bellman-ford-and-dijkstra-s-algorithm-w-brief-explanation-and-analysis/

# Using multiplication of vertices
def maxProbability(n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
    graph = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, succProb[i]))
        graph[v].append((u, succProb[i]))

    probabilities = [0] * n
    probabilities[start_node] = 1  # start with probability 1 at the start node
    max_heap = [(-probabilities[start_node], start_node)]  
    while max_heap:
        current_probability, vertex = heapq.heappop(max_heap)
        current_probability = -current_probability 

        if vertex == end_node:
            return current_probability

        for adj_v, weight in graph[vertex]:
            new_probability = current_probability * weight
            if new_probability > probabilities[adj_v]:
                probabilities[adj_v] = new_probability
                # make heap prioritize maximum value i.e. using max_heap 
                heapq.heappush(max_heap, (-new_probability, adj_v))
    return 0


# Aplying logarithm to transform to a sum.
def maxProbability(n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
    graph = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, np.log(succProb[i])))
        graph[v].append((u, np.log(succProb[i])))

    probabilities = [-maxsize] * n
    probabilities[start_node] = 0  # start with probability log(1) at the start node
    max_heap = [(-probabilities[start_node], start_node)]  
    while max_heap:
        current_probability, vertex = heapq.heappop(max_heap)
        current_probability = -current_probability 

        if vertex == end_node:
            return np.exp(current_probability)

        for adj_v, weight in graph[vertex]:
            new_probability = current_probability + weight
            if new_probability > probabilities[adj_v]:
                probabilities[adj_v] = new_probability
                # make heap prioritize maximum value
                heapq.heappush(max_heap, (-new_probability, adj_v))
    return 0