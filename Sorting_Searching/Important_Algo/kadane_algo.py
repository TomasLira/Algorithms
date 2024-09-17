def maximum_subarray(nums):
    max_sum = nums[0]
    left,current_sum = 0,0
    start_idx,end_idx = 0,0
    for right in range(len(nums)):
        current_sum += nums[right]
        # Ignore everything to the right
        if current_sum < 0:
            current_sum = 0
            right +=1
            left = right
        if current_sum > max_sum:
            max_sum = current_sum
            start_idx,end_idx = left,right
    return [start_idx,end_idx]


def maxSubArray(nums: list[int]) -> int:
    maximum_sum,current_sum = float("-inf"),0
    for num in nums:
        current_sum = max(num,current_sum+num)
        maximum_sum = max(current_sum,maximum_sum)  
    return maximum_sum
        
