# Modify the function to count the number of unique lists
from collections import defaultdict

def count_unique_lists(nums_l):
    hash_table = defaultdict(lambda: (0, -1))
    for idx, nums in enumerate(nums_l):
        for num in nums:
            count, prev_idx = hash_table[num]
            if prev_idx != idx:
                hash_table[num] = (count + 1, idx)
    
    unique_numbers = {}
    for num, (count, _) in hash_table.items():
        if count == 1:
            unique_numbers[num] = idx
    
    unique_count = 0
    for nums in nums_l:
        is_unique = True
        for num in nums:
            if num not in unique_numbers:
                is_unique = False
                break
        if is_unique:
            unique_count += 1
    
    return unique_count

test_cases = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],      # all unique lists
    [[1, 2], [2, 3], [4, 5]],               # only [4, 5] is unique
    [[1, 2, 3], [1, 2, 3], [4, 5, 6]],      # only [4, 5, 6] is unique
    [[1, 2], [2, 1], [3, 4]],               # only [3,4]
    [[1], [2], [1, 2], [3, 4], [5]],        # [3, 4], [5] are unique
]

# Running the tests again with the modified function
unique_counts = [count_unique_lists(tc) for tc in test_cases]
print(unique_counts)
