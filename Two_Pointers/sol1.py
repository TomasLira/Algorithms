from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left,right = 0, len(nums)-1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left,right]