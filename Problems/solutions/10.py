# Solution 1 O(n) Time O(n) Space
def missing_pos(nums):
    pivot  = 0
    smaller_idx = -1
    for current_idx in range(len(nums)):
        if nums[current_idx] <= pivot:
            smaller_idx += 1
            nums[current_idx],nums[smaller_idx]= nums[smaller_idx],nums[current_idx]
    non_neg_idx = smaller_idx + 1
    # All elements after index are positive 
    if non_neg_idx >= len(nums):
        return 0
    pos_set = (nums[non_neg_idx:])
    # Iterates through all consecutive numbers
    for i in range(1,len(nums)):
        if i not in pos_set:
            return i
    return max(nums) + 1
    
print(missing_pos([-1,-2,-3,1,12]))    
    

    
    
    
