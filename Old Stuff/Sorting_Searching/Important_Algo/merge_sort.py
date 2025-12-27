from typing import List

# recursive
def merge(left: List[int],right: List[int])-> List[int]:
    if not right:
        return left
    if not left:
        return right
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:],right)
    else:
        return [right[0]] + merge(left,right[1:])

def merge_sort_rec(nums: List[int])->List[int]:
    if len(nums) <= 1:
        return nums
    middle: int = len(nums) // 2
    left: List[int] = merge_sort_rec(nums[:middle])
    right: List[int] = merge_sort_rec(nums[middle:])
    return merge(left,right)