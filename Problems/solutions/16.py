# Solution 1 O(n) time
from sys import maxsize
def smallest_subarray(nums,target):
    smallest_subarray = maxsize
    current_sum = 0
    left,total = 0,0
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            smallest_subarray = min(smallest_subarray,right - left + 1)
            current_sum -= nums[left]
            left += 1
    return smallest_subarray if smallest_subarray != maxsize else 0
        
        
# Solution 2 O(n) time 
def smallest_subarray(nums,target):
    # Sliding window has undefined size
    left,size = 0,0
    current_sum,smallest_size = 0,len(nums) +1
    for right,num in enumerate(nums):
        current_sum += num
        size += 1
        while current_sum >= target:
            if current_sum >= target:
                smallest_size = min(smallest_size,size)
            current_sum -= nums[left]
            left += 1
            size -= 1            
    return smallest_size if smallest_size != len(nums)+1 else 0    

print(smallest_subarray([2,3,1,2,4,3],7))



# This question is a variation when equals to target
def smallest_subarray(nums,target):
    # Sliding window has undefined size
    left,size = 0,0
    current_sum,smallest_size = 0,float('inf')
    for right,num in enumerate(nums):
        current_sum += num
        size += 1
        while current_sum > target:
            current_sum -= nums[left]
            left += 1
            size -= 1            
        if current_sum == target:
            smallest_size = min(smallest_size,size)
    return smallest_size if smallest_size != len(nums) else 0    


# print(smallest_subarray([1,2,3,4,5],11))
            
            
            
        