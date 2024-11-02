class BST:
    def __init__(self, value=None) -> None:
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

    def find_node(self, target):
        current_node = self
        while current_node is not None:
            if current_node.value == target:
                return current_node
            elif target < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None  # Node not found

    def insert_node(self, new_value):
        if self.value is None:
            self.value = new_value
            return

        if new_value < self.value:
            if self.left is None:
                self.left = BST(new_value)
                self.left.parent = self
            else:
                self.left.insert_node(new_value)
        else:
            if self.right is None:
                self.right = BST(new_value)
                self.right.parent = self
            else:
                self.right.insert_node(new_value)

def find_closest(root, target):
    if root is None:
        return None 

    closest_value = root.value
    current_node = root

    while current_node is not None:
        if abs(current_node.value - target) < abs(closest_value - target):
            closest_value = current_node.value

        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest_value

root = BST(10)
root.insert_node(15)
root.insert_node(13)
root.insert_node(21)
root.insert_node(20)
root.insert_node(22)
root.insert_node(5)
root.insert_node(8)
root.insert_node(3)

target = 18
closest = find_closest(root, target)
print(f"The closest value to {target} in the BST is {closest}.")