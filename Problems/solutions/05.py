from sys import maxsize

class BST:
    def __init__(self, value=None) -> None:
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

    def find_node(self, target):
        current_node = self
        if current_node is None:
            return None
        if current_node.value != target and current_node.right is None and current_node.left is None:
            return False
        if current_node.value == target:
            return current_node
        elif current_node.value < target:
            return current_node.right.find_node(target) if current_node.right else None
        else:
            return current_node.left.find_node(target) if current_node.left else None

    def insert_node(self, new_value):
        current_node = self
        if current_node is None:
            new_node = BST(new_value)
            return
        if current_node.value < new_value:
            if current_node.right is None:
                new_node = BST(new_value)
                new_node.parent = current_node
                current_node.right = new_node
            else:
                current_node.right.insert_node(new_value)
        elif current_node.value > new_value:
            if current_node.left is None:
                new_node = BST(new_value)
                new_node.parent = current_node
                current_node.left = new_node
            else:
                current_node.left.insert_node(new_value)

def store_nodes_in_order(node, node_list):
    if node is not None:  
        store_nodes_in_order(node.left, node_list) 
        node_list.append(node.value)  
        store_nodes_in_order(node.right, node_list)


def get_smallest(nums):
    smallest_sum = maxsize
    for idx in range(1,len(nums)):
        smallest_sum = min(abs(nums[idx]-nums[idx-1]),smallest_sum)
    return smallest_sum
        
    
root = BST(10)
root.insert_node(15)
root.insert_node(13)
root.insert_node(21)
root.insert_node(20)
root.insert_node(22)
root.insert_node(5)
root.insert_node(8)
root.insert_node(3)
nums = []
store_nodes_in_order(root,nums)
print(get_smallest(nums))