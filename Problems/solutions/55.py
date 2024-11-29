def dfs(n:int,edges: list[tuple[int,int,int]],L1:list[int]):
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
                parents[adj_v] = vertex
                dfs_helper(adj_v)    
        post_order[vertex] = end_time[0]
        end_time[0] += 1
        
    for vertex in range(n):
        if pre_order[vertex] == -1:
            dfs_helper(vertex)
    
                
    def odd_descendants(root, tree, L1):
        L2 = []
        def dfs(node, parent):
            count = 0
            for child in tree[node]:
                if child != parent:
                    count += dfs(child, node) + (child in L1)
            if (node in L1) or (count % 2 == 1):
                L2.append(node)
            return count
        dfs(root, -1)
        return L2
    
    def odd_ancestors(root, tree, L1):
        L2 = []
        ancestors = set()

        def dfs(node, parent):
            if node in L1 or len(ancestors) % 2 == 1:
                L2.append(node)
            ancestors.add(node)
            for child in tree[node]:
                if child != parent:
                    dfs(child, node)
            ancestors.remove(node)
        
        dfs(root, -1)
        return L2

    def odd_older_cousins(root, tree, L1, ages):
        L2 = []
        def dfs(node, parent, older_count):
            if node in L1 or older_count % 2 == 1:
                L2.append(node)
            for child in tree[node]:
                if child != parent:
                    dfs(child, node, older_count + (ages[child] < ages[node]))
        
        dfs(root, -1, 0)
        return L2


        