def k_closest(nums,x):
    nums = sorted(nums)
    left,current_diff = 0,0
    max_size = 1
    for right in range(1,(len(nums))):
        # Every pair in list by construct will be smaller than x if current_diff < x
        current_diff = nums[right] - nums[left]
        while left < right and current_diff > x:
            left += 1
            current_diff = nums[right] - nums[left]
        max_size = max(max_size,right - left +1)
    return max_size    