from typing import List

def count_inversions(nums: List[int]):
    if len(nums) <= 1:
        return nums, 0
    middle: int = len(nums) // 2
    left, left_inversions = count_inversions(nums[:middle])
    right, right_inversions = count_inversions(nums[middle:])
    counter = left_inversions + right_inversions
    
    def merge(left: List[int], right: List[int]) -> List[int]:
        nonlocal counter
        sorted_list = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                counter += 1
                j += 1
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list

    sorted_list = merge(left, right)
    return sorted_list, counter

print(count_inversions([1, 2, 3, 4, 5]))
