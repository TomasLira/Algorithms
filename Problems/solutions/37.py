#O(V+E) time O(V) space
# Optimal if we are dealing with degree 2 vertices
def greedy_coloring(graph):
    v_len = len(graph)
    colors = [-1]*v_len
    
    for v in range(v_len):
        used_colors = set()
        for adj_v in graph[v]:
            if colors[adj_v] != -1:
                used_colors.add(colors[adj_v])
        color = 1
        while color in used_colors:
            color += 1
        colors[v] = color
    
    return max(colors)  

graph = [[1,2],[0,2],[0,1]]
print(greedy_coloring(graph)) 