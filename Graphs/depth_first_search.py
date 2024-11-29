def dfs(n:int,edges: list[tuple[int,int,int]]):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        #graph[v].append(u)
    pre_order, post_order, parents = [-1] * n, [-1] * n, [-1] * n
    start_time, end_time = [0], [0]
    
    
    # v_j adj and v_i vertex
    # adj contem vertex --> backedge
    # adj contido vertex --> forward
    def dfs_helper(vertex):
        pre_order[vertex] = start_time[0]
        start_time[0] += 1
        
        for adj_v in graph[vertex]:
            if pre_order[adj_v] == -1:
                print(f"Normal Tree edge: {vertex} --> {adj_v}")
                parents[adj_v] = vertex
                dfs_helper(adj_v)
            else:
                if post_order[adj_v] ==-1:
                    print(f"Back edge: {vertex} --> {adj_v}")
                # post_order[vertex] > post_order[adj_v]
                else:
                    if pre_order[vertex] < pre_order[adj_v]:
                        print(f"Forward edge: {vertex} --> {adj_v}")
                    elif pre_order[vertex] > pre_order[adj_v]:
                        print(f"Cross edge: {vertex} --> {adj_v}")
        post_order[vertex] = end_time[0]
        end_time[0] += 1
        
    for vertex in range(n):
        if pre_order[vertex] == -1:
            dfs_helper(vertex)
        
dfs(6, [
    [0, 1], 
    [0, 2],  
    [1, 3],  
    [1, 4],  
    [3, 4],  
    [2, 5],  
    [0, 5]   
])