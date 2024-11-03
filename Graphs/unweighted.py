def check_path(graph: list[list[int]], path: list[int]) -> bool:
    if not path:
        return True  
    start_v = path[0]
    idx = 1 
    
    while idx < len(path):
        found = False
        for adj_v in graph[start_v]:
            if adj_v == path[idx]:
                start_v = adj_v
                idx += 1
                found = True
                break
        if not found:
            return False     
    return True

# we want to check if nodes in graph are topologically sorted 
def check_numeration_topological(graph: list[list[int]]):
    for i in range(len(graph)):
        for adj_vertex in graph[i]:
            if i > adj_vertex:
                return False       
