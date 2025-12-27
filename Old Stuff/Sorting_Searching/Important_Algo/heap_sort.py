from typing import List, Optional

class MinHeap:
    nodes: List[int]

    def __init__(self) -> None:
        self.nodes = []

    def __len__(self) -> int:
        return len(self.nodes)

    def get_parent_idx(self, child_idx: int) -> int:
        if child_idx == 0:
            raise IndexError("Root node has no parent.")
        return (child_idx - 1) // 2

    def get_left_child_idx(self, parent_idx: int) -> Optional[int]:
        left_child_idx = 2 * parent_idx + 1
        if left_child_idx < len(self.nodes):
            return left_child_idx
        return None

    def get_right_child_idx(self, parent_idx: int) -> Optional[int]:
        right_child_idx = 2 * parent_idx + 2
        if right_child_idx < len(self.nodes):
            return right_child_idx
        return None

    def has_parent(self, child_idx: int) -> bool:
        return child_idx > 0

    def left_child(self, parent_idx: int) -> Optional[int]:
        left_child_idx = self.get_left_child_idx(parent_idx)
        if left_child_idx is not None:
            return self.nodes[left_child_idx]
        return None

    def right_child(self, parent_idx: int) -> Optional[int]:
        right_child_idx = self.get_right_child_idx(parent_idx)
        if right_child_idx is not None:
            return self.nodes[right_child_idx]
        return None

    def get_root(self) -> Optional[int]:
        if not self.nodes:
            return None
        return self.nodes[0]

    def get_parent(self, child_idx: int) -> int:
        if not self.has_parent(child_idx):
            raise IndexError(f"Child at index {child_idx} has no parent.")
        parent_idx: int = self.get_parent_idx(child_idx)
        return self.nodes[parent_idx]

    def bubble_up(self, child_idx: Optional[int] = None) -> None:
        if child_idx is None:
            child_idx: int = len(self.nodes) - 1

        while self.has_parent(child_idx):
            parent_idx: int = self.get_parent_idx(child_idx)
            if self.nodes[parent_idx] > self.nodes[child_idx]:
                self.nodes[parent_idx], self.nodes[child_idx] = self.nodes[child_idx], self.nodes[parent_idx]
                child_idx = parent_idx
            else:
                break

    def heapify(self, parent_idx: int = 0) -> None:
        smallest_idx: int = parent_idx

        left_child_idx = self.get_left_child_idx(parent_idx)
        right_child_idx = self.get_right_child_idx(parent_idx)

        if left_child_idx is not None and self.nodes[left_child_idx] < self.nodes[smallest_idx]:
            smallest_idx: int = left_child_idx

        if right_child_idx is not None and self.nodes[right_child_idx] < self.nodes[smallest_idx]:
            smallest_idx: int = right_child_idx

        if smallest_idx != parent_idx:
            self.nodes[smallest_idx], self.nodes[parent_idx] = self.nodes[parent_idx], self.nodes[smallest_idx]
            self.heapify(smallest_idx)

    def insert(self, value: int) -> None:
        self.nodes.append(value)
        self.bubble_up()

    def extract_min(self) -> Optional[int]:
        if not self.nodes:
            return None
        if len(self) == 1:
            return self.nodes.pop()

        min_value = self.nodes[0]
        # Removed top element and subtituted with the right-most leaf, i.e. the last elem in list
        self.nodes[0] = self.nodes.pop()
        self.heapify()
        return min_value
    
    def heap_sort(self) -> List[int]:
        sorted_array = []
        while len(self.nodes) > 0:
            min_value: int = self.extract_min()
            sorted_array.append(min_value)
        return sorted_array

def test_min_heap():
    # Test 1: Insert elements into the heap and check the min value
    heap = MinHeap()
    heap.insert(10)
    heap.insert(4)
    heap.insert(15)
    heap.insert(20)
    heap.insert(0)
    assert heap.get_root() == 0, "Test 1 Failed: Root should be the smallest element (0)"

    # Test 2: Extract min element and verify the heap structure
    min_value = heap.extract_min()
    assert min_value == 0, "Test 2 Failed: Extracted min should be 0"
    assert heap.get_root() == 4, "Test 2 Failed: New root after extracting min should be 4"

    # Test 3: Extract remaining elements and check order
    min_value = heap.extract_min()
    assert min_value == 4, "Test 3 Failed: Extracted min should be 4"
    min_value = heap.extract_min()
    assert min_value == 10, "Test 3 Failed: Extracted min should be 10"
    min_value = heap.extract_min()
    assert min_value == 15, "Test 3 Failed: Extracted min should be 15"
    min_value = heap.extract_min()
    assert min_value == 20, "Test 3 Failed: Extracted min should be 20"
    assert len(heap) == 0, "Test 3 Failed: Heap should be empty after all extractions"

    # Test 4: Extract from an empty heap
    min_value = heap.extract_min()
    assert min_value is None, "Test 4 Failed: Extracting from an empty heap should return None"

    # Test 5: Insert elements and verify heap property
    heap.insert(8)
    heap.insert(3)
    heap.insert(5)
    heap.insert(12)
    heap.insert(2)
    heap.insert(1)
    assert heap.get_root() == 1, "Test 5 Failed: Root should be 1"
    heap.extract_min()
    assert heap.get_root() == 2, "Test 5 Failed: After extracting 1, root should be 2"

    # Test 6: Inserting a single element and removing it
    heap2 = MinHeap()
    heap2.insert(42)
    assert heap2.extract_min() == 42, "Test 6 Failed: Inserting and extracting a single element should return that element"
    assert heap2.extract_min() is None, "Test 6 Failed: Extracting from an empty heap should return None"
    
    heap3 = MinHeap()
    heap3.insert(8)
    heap3.insert(3)
    heap3.insert(5)
    heap3.insert(12)
    heap3.insert(2)
    heap3.insert(1)
    print(f"Sorted Heap: {heap3.heap_sort()}")

test_min_heap()

