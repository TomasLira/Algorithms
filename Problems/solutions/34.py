# Solution 1 O(n)
def findUnsortedSubarray(nums):
    start = -1
    end = -1
    for idx in range(1, len(nums)):
        if nums[idx] < nums[idx - 1]:
            if start == -1:
                start = idx - 1
            end = idx
    if start == -1:
        return 0 
    
    min_subarray = min(nums[start:end+1])
    max_subarray = max(nums[start:end+1])
    for left in range(0,start):
        if nums[left] > min_subarray:
            start = left
            break
    for right in range(len(nums)-1,start-1,-1):
        if nums[right] < max_subarray:
            end = right 
            break
    return end - start + 1

print(findUnsortedSubarray([2,6,4,1,10,9,15])) 
