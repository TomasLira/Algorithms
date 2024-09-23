# Solution 1 O(nm) Time
from collections import defaultdict
def unique_lists(nums_l: list[list[int]]):
    # Default value if element not found
    hash_table = defaultdict(lambda: (0, -1))
    
    # Only register the frequency if in diff lists
    for idx, nums in enumerate(nums_l):
        for num in nums:
            count, prev_idx = hash_table[num]
            if prev_idx != idx:
                hash_table[num] = (count + 1, idx)
    
    unique_numbers = []
    # Get unique elements
    for num, (count, _) in hash_table.items():
        if count == 1:
            unique_numbers.append(num)
    
    result = []
    for nums in nums_l:
        is_unique = True
        for num in nums:
            if num not in unique_numbers:
                is_unique = False
                break
        if is_unique:
            result.append(nums)
    
    return result