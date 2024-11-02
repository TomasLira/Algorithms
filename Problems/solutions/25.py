from typing import Optional
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Using DFS
class Solution:
    def clone_node(self, original_node: 'Node', visited_nodes: dict) -> 'Node':
        cloned_node = Node(original_node.val)
    
        visited_nodes[original_node.val] = cloned_node
        
        for neighbor in original_node.neighbors:
            # Conditional only changes if we'll create or not a Node
            if neighbor.val not in visited_nodes:
                cloned_node.neighbors.append(self.clone_node(neighbor, visited_nodes))
            else:
                # Dict stores the class Node
                cloned_node.neighbors.append(visited_nodes[neighbor.val])
        
        return cloned_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        visited_nodes = {}
        
        return self.clone_node(node, visited_nodes)
    
# Using BFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        visited_nodes = {}
        queue = deque([node])
        cloned_nodes = {node.val: Node(node.val, [])}

        while queue:
            current_node = queue.popleft()
            current_clone = cloned_nodes[current_node.val]

            for adj_node in current_node.neighbors:
                if adj_node.val not in cloned_nodes:
                    cloned_nodes[adj_node.val] = Node(adj_node.val, [])
                    queue.append(adj_node)
                current_clone.neighbors.append(cloned_nodes[adj_node.val])
                
        return cloned_nodes[node.val]