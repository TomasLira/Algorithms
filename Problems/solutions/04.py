def least_biggest(nums):    
    # All elements bigger than len(nums) are discarded
    # Each element represented by index
    freq_list = [0] * (len(nums) + 1)
    
    for num in nums:
        if num <= len(nums):
            freq_list[num] += 1
    
    accumulator = 0
    # Traverse from the back, accumulate frequencies
    for idx in range(len(freq_list) - 1, -1, -1):
        freq_list[idx] += accumulator
        accumulator = freq_list[idx]
    
    # Find the largest x so x numbers are >= x
    for idx in range(len(freq_list) - 1, -1, -1):
        if freq_list[idx] >= idx:
            return nums[idx]
    return -1

print(least_biggest([1, 2, 3, 5,5,5,5, 4]))  
