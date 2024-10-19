from typing import List, Optional

def dfs(graph: List[List[int]]) -> None:
    v_len = len(graph)
    
    colors: List[str] = ['W'] * v_len  # W = White (unvisited), G = Gray (in progress), B = Black (finished)
    parent: List[Optional[int]] = [None] * v_len
    discovery_time: List[int] = [-1] * v_len
    finish_time: List[int] = [-1] * v_len
    time = [0] 
    dfs_tree = {}

    def dfs_visit(start_v: int) -> None:
        colors[start_v] = 'G'
        time[0] += 1
        discovery_time[start_v] = time[0]
        dfs_tree[start_v] = []
        
        for adj_v in graph[start_v]:
            if colors[adj_v] == 'W':  
                parent[adj_v] = start_v
                #print(f'Vertex visited: {adj_v}')
                dfs_tree[start_v].append(adj_v)
                dfs_visit(adj_v)
        
        colors[start_v] = 'B'
        time[0] += 1
        finish_time[start_v] = time[0]
    
    # handle disconnected graphs
    for vertex in range(v_len):
        if colors[vertex] == 'W':
            dfs_visit(vertex)
            
    def print_tree(vertex: int, indent: str = "") -> None:
        print(f"{indent}Vertex {vertex}: Discovery Time = {discovery_time[vertex]}, Finish Time = {finish_time[vertex]}")
        
        for i, child in enumerate(dfs_tree.get(vertex, [])):
            if i == len(dfs_tree[vertex]) - 1: 
                print(f"{indent}  └── {child}")
            else:
                print(f"{indent}  ├── {child}")
            print_tree(child, indent + "  |  ")

    print("DFS Tree Visualization:")
    for vertex in range(v_len):
        if parent[vertex] is None: 
            print_tree(vertex)

graph = [
    [1, 2],    # Vertex 0 is connected to 1 and 2
    [0, 3,4],    # Vertex 1 is connected to 0, 3 and 4
    [0, 3],    # Vertex 2 is connected to 0 and 3
    [1, 2,4], # Vertex 3 is connected to 1, 2
    [1,2,3] # Vertex 4 is connected to 1,2,3
]
dfs(graph)


