def numIslands(grid: list[list[str]]) -> int:
    visited = set()
    island_num = 0

    def dfs(i, j):
        # Used the Boolean complement operation
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == '0':
            return
        visited.add((i, j))
        dfs(i + 1, j)  
        dfs(i - 1, j)  
        dfs(i, j + 1) 
        dfs(i, j - 1) 

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(i, j)
                island_num += 1 
    return island_num


class UF:
    def __init__(self, n):
        # Each node is its own parent at initialization
        self.parent = [i for i in range(n)]
        self.size = n
    
    def union(self, i, j):
        parent_i, parent_j = self.find(i), self.find(j)
        if parent_i != parent_j:
            self.size -= 1
            self.parent[parent_j] = parent_i
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
            

def numIslands(grid: list[list[str]]) -> int:
    # The goal is to treat each cell with '1' as a node
    # and connect the nodes that are adjacent to each other using union find
    dict_set = {}
    # Unique value for each node
    idx = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dict_set[(i, j)] = idx
                idx += 1

    uf = UF(len(dict_set))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                # Analyze down and left neighbors
                if i > 0 and grid[i - 1][j] == '1':
                    uf.union(dict_set[(i, j)], dict_set[(i - 1, j)])
                if j > 0 and grid[i][j - 1] == '1':
                    uf.union(dict_set[(i, j)], dict_set[(i, j - 1)])

    return uf.size
