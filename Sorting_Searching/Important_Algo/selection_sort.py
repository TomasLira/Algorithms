#https://en.wikipedia.org/wiki/Selection_sort
from typing import List

#Iterative:
def selection_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        min_index: int = i 
        for j in range(i + 1, len(nums)): 
            if nums[j] < nums[min_index]: 
                min_index: int = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

# Recursive:
def find_min_index(nums: List[int], start: int) -> int:
    return start + min(range(len(nums) - start), key=lambda i: nums[start + i])

def selection_sort_rec(nums: List[int]) -> List[int]:
    if not nums:
        return []
    min_index = find_min_index(nums, 0)
    # sum of lists results in concatenation
    return [nums[min_index]] + selection_sort(nums[:min_index] + nums[min_index + 1:])
