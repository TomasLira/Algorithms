import heapq
from sys import maxsize
def smallest_range(nums_list):
    heap = []
    max_val =  -maxsize
    for list_idx,nums in enumerate(nums_list): 
        heapq.heappush(heap,(nums[0],list_idx,0)) # value, list_idx, and elem_idx
        max_val = max(max_val,nums[0])
    range_start,range_end = -maxsize,maxsize
    
    while heap:
        # Sliding window for heap
        min_val,list_idx,elem_idx = heapq.heappop(heap)
        if max_val - min_val < range_end - range_start:
            range_end = max_val
            range_start = min_val
        if elem_idx + 1 < len(nums_list[list_idx]):
            next_element = nums_list[list_idx][elem_idx+1]
            heapq.heappush(heap,(next_element,list_idx,elem_idx+1))
            max_val = max(max_val,next_element)
        else:
            break
        print(min_val,max_val)
    return [range_start,range_end]
            
nums = [
    
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]

resultado = smallest_range(nums)
print(f"Menor intervalo: {resultado}")
