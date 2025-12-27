def three_sum(nums,target):
    result = []
    nums.sort()
    for left in range(len(nums)):
        # Filter duplicate elements
        if left > 0 and nums[left] == nums[left-1]:
            continue
        start,end = left+1,len(nums)-1
        while start < end:
            total_sum = nums[left] + nums[start] + nums[end]
            if  total_sum < target:
                start +=1
            elif  total_sum > target:
                end -= 1
            else:
                result.append(nums[left],nums[start],nums[end])
                left += 1
                # Edge case when values are repeated
                while nums[start] == nums[start-1] and start < end:
                    start += 1
    return result