def depth_first_search(n: int, edges: list[list[int]]):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    pre_order, post_order, parents = [-1] * n, [-1] * n, [-1] * n
    start_time, end_time = [0], [0]
    processed_edges = set() 
    
    def dfs_helper(vertex):
        #print(vertex,pre_order,post_order)
        pre_order[vertex] = start_time[0]
        start_time[0] += 1 

        for adj_v in graph[vertex]:
            if (vertex, adj_v) in processed_edges or (adj_v, vertex) in processed_edges:
                continue            
            processed_edges.add((vertex, adj_v))
            if pre_order[adj_v] == -1: 
                print(f"Tree edge: {vertex} -> {adj_v}") 
                parents[adj_v] = vertex
                dfs_helper(adj_v)
            # pre_order[adj_v] <=, cuz it has been discovered before vertex
            else:
                # i.e. adj_v is already known, so vertex is in adj_v recursive stack, tehrefore post_order[vertex] < post_order[adj_v]
                # and parents[vertex] != adj_v
                if post_order[adj_v] == -1:
                    print(f"Back edge: {vertex} -> {adj_v}")
                else:
                    # ...
                    if pre_order[vertex] < pre_order[adj_v]:
                        print(f"Forward edge: {vertex} -> {adj_v}")
                    #...
                    elif pre_order[vertex] > pre_order[adj_v]:
                        print(f"Cross edge: {vertex} -> {adj_v}")
        post_order[vertex] = end_time[0]
        end_time[0] += 1 
        
    for vertex in range(n):
        if pre_order[vertex] == -1:
            dfs_helper(vertex)

depth_first_search(6, [
    [0, 1], 
    [0, 2],  
    [1, 3],  
    [1, 4],  
    [3, 4],  
    [2, 5],  
    [0, 5]   
])
