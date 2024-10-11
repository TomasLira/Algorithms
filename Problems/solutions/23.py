from sys import maxsize
# Solution O(n) Time
def maximum_prod(nums):
        max1 = max2 = max3 = -maxsize
        min1 = min2 = maxsize
        
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max2 * max3 * max1, min1 * min2 * max1)
        
# If subarray had to be contiguous
def maximum_prod(nums):            
    current_prod,maximum_prod = 1,-maxsize
    for right in range(2,len(nums)):
        current_prod = nums[right]*nums[right-1]*nums[right-2]       
        maximum_prod = max(maximum_prod,current_prod)
    return maximum_prod