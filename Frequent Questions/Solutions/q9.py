# O problema pode ser resolvido de três formas diferentes.
#Busca binária:
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
def binary_search(nums, target):
    left, right = 0, len(nums) - 1 
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            return middle
    return None


def q9_1(nums: list[int])-> list[int]:
    ...
            
        
        
        
        
    
    
    
    
    