# Solution 1 O(n) Time
def pair_sum(nums,target):
    hash_table = {}
    for num in nums:
        hash_table[num] = target - num  
    for num in nums:
        # See if num is another nums complement
        complement = hash_table[num]
        if complement is not None and complement != num:
            return [num,complement]
    return None     

# Solution 2 O(n) Time
def pair_sum(nums,target):
    hash_table = {}
    for num in nums:
        complement = target - num
        # Automatically treats the case when two nums are at same pos
        if complement in hash_table:
            return [complement,num]
        # True is a dummy value
        hash_table[num] = True
    