class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = n
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.size -= 1
            self.parent[root_j] = root_i
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    uf = UF(len(edges) + 1)
    for v1, v2 in edges:
        if uf.find(v1) == uf.find(v2):
            return [v1, v2]
        uf.union(v1, v2)
    return None

print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
