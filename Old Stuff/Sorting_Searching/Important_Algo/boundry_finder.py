from typing import Tuple

def find_left_boundry(nums: list[int],target:int)->int:
    left,right = 0,len(nums) -1
    while left <= right:
        middle = left + (right-left)//2
        # gets the leftmost element
        if nums[middle] < target:
            left  = middle + 1
        else:
            right = middle - 1
    return left

def find_right_boundry(nums: list[int],target:int)->int:
    left,right = 0,len(nums)-1
    while left <= right:
        middle = left + (right-left)//2
        # gets rightmost element
        if nums[middle] <= target:
            left = middle + 1
        else:
            right = middle - 1
    return right


def find_boundry(nums: list[int],target: int)->Tuple[int,int]:
    left_b = find_left_boundry(nums,target)
    right_b = find_right_boundry(nums,target)
    
    if left_b <= right_b and left_b <= len(nums):
        return (left_b,right_b)
    return (-1,-1)

print(find_boundry([1,2,2,4,5,6,6,6,6,7,8,13],6))