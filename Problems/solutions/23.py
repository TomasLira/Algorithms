def majority_element(nums):
    count_num,count = 0,0
    # The biggest number will appear more than n/2 times
    for num in nums:
        if count == 0:
            count_num = num
            count += 1
        elif count_num != num:
            count -= 1
        else:
            count += 1
    return count_num

