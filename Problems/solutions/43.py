from sys import maxsize

def maximum_prod(nums):
    max1 = max2 = -maxsize  
    min1 = min2 = maxsize  

    for num in nums:
        if num >= 0:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        else:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

    max_pos_pair = max1 * max2
    max_neg_pair = min1 * min2
    return max((max1,max2),(min1,min2))

print(maximum_prod([-100,-98,-1,2,3,4]))

        
    
        
        
        
        
    
        

print(maximum_prod([-100,-98,-1,2,3,4]))

            
    

# If subarray had to be contiguous
def maximum_prod(nums):            
    current_prod,maximum_prod = 1,-maxsize
    for right in range(2,len(nums)):
        current_prod = nums[right]*nums[right-1]*nums[right-2]       
        maximum_prod = max(maximum_prod,current_prod)
    return maximum_prod