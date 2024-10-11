from collections import deque

class Graph:
    def __init__(self,directed=False) -> None:
        self.adj_list = {}
        self.directed = directed
    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            
    def add_edge(self,v1,v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        if not self.directed:
            self.adj_list[v2].append(v1)
            
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        if not self.directed and v2 in self.adj_list and v1 in self.adj_list[v2]:
            self.adj_list[v2].remove(v1)
    
    def remove_vertex(self,v):
        if v in self.adj_list:
            for other_v in list(self.adj_list.keys()):
                if v in self.adj_list[other_v]:
                    self.adj_list[other_v].remove(v)
            del self.adj_list[v]   
            
    def breath_first_search(self,start_v):
        queue = []
        if start_v not in self.adj_list:
            print(f"vertex {start_v} not in graph!")
            return
        visited = set()
        queue = deque([start_v])
        nodes_list = []
        
        while queue:
            current_v = queue.popleft()
            if current_v not in visited:
                visited.add(current_v)
                nodes_list.append(current_v)
            for neighbor in self.adj_list[current_v]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return nodes_list
        
    def depth_first_search(self, start_v):
        if start_v not in self.adj_list:
            print(f"Vertex {start_v} not in the graph!")
            return []

        visited = set()  
        nodes_list = []  
        
        def dfs(v):
            visited.add(v) 
            nodes_list.append(v)  
            for neighbor in self.adj_list[v]:
                if neighbor not in visited: 
                    dfs(neighbor)
        dfs(start_v)
        return nodes_list 
    
    def is_valid_path(self, path):
        if not path:
            return False
        v1 = path[0]
        
        for idx in range(1, len(path)):
            v2 = path[idx]
            # O(n) comparison
            if v2 not in self.adj_list[v1]: 
                return False
            v1 = v2  
        return True
    
    
    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

