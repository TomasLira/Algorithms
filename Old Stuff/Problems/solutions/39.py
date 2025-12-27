# O(...) Solution only using adj list
def squared_graph(graph):
    edges = set()
    for u in range(len(graph)):
        for v in graph[u]:
            for w in graph[v]:
                if u != w:  
                    edges.add((u, w))
    return edges

graph = [[1, 2], [0], [1, 3,4],[],[]]
print(squared_graph(graph))