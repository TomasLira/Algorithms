def q1(nums: list[int])-> int:
    maximum_sum,current_sum = float("-inf"),0
    for num in nums:
        current_sum = max(num,current_sum+num)
        maximum_sum = max(current_sum,maximum_sum)  
    return maximum_sum