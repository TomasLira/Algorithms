def q2(nums: list[int])-> list[int]:
    duplicates = {}
    for idx,num in enumerate(nums):
        if num not in duplicates :
            duplicates[num] = 1
        else:
            del nums[idx]
    return nums


print(q2([1,1,2,3,5,5]))
            
            