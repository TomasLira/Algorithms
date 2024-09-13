def q5(nums: list[int])-> list[int]:
    pivot = 0
    smaller_idx = -1
    for current_idx  in range(len(nums)):
        if nums[current_idx] <= pivot:
            smaller_idx += 1
            nums[current_idx],nums[smaller_idx] = nums[smaller_idx],nums[current_idx]
    return nums

#print(q5([1,3,4,56,-3,5,-1,24,2-12]))

        
            
            
            
            
        
    