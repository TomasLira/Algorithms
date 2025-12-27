import random
from sys import maxsize

def find_pair_optimized(nums):
    left,right = 0,len(nums) - 1 
    indices = (-1,-1)
    max_eq = -maxsize
    while left < right:
        # tradeoff of starting as max indices having possibly small nums[idx]
        # iteration will shrink |i,j| and make min() bigger!
        eq = abs(left - right)*min(nums[left],nums[right])
        if eq >= max_eq:
            indices  = (left,right)
            max_eq = eq
        # maximize min() pois abs() sempre será constante indep
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return indices