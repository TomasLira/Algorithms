class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = n