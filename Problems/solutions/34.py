from collections import deque

def longest_path(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(vertex):
        queue = deque([(vertex, 0)])  
        visited = set([vertex])       
        max_depth_node = vertex
        max_distance = 0

        while queue:
            current, dist = queue.popleft()
            if dist > max_distance:
                max_depth_node = current
                max_distance = dist

            for adj_v in graph[current]:
                if adj_v not in visited:
                    queue.append((adj_v, dist + 1))
                    visited.add(adj_v)

        return max_depth_node, max_distance

    node1, _ = bfs(0)
    _, longest_distance = bfs(node1)
    
    return longest_distance