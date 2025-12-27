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

tree = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: []
}

L1 = [1, 3]
ages = [30, 40, 25, 35, 20] 
root = 0

print(odd_descendants(root, tree, L1))
print(odd_ancestors(root, tree, L1))
print(odd_older_cousins(root, tree, L1, ages))
