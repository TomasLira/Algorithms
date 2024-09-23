# Solution 1 O(n) Time
def pair_sum(nums,target):
    hashmap = {}
    for idx,num in enumerate(nums):
        hashmap[target - num] = idx
    for idx,num in enumerate(nums):
        if num in hashmap and idx != hashmap[num]:
            return [idx,hashmap[num]]
    return []  

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
    