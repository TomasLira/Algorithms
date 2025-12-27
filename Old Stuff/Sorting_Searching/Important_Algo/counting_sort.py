from typing import List

def counting_sort(nums: List[int]) -> List[int]:
    if not len(nums):
        return []
    max_num = max(nums)
    freq_list = [0] * (max_num + 1)
    sorted_list = [0] * len(nums)
    
    for num in nums:
        # Each number is represented as an index position
        freq_list[num] += 1
        
    for idx in range(1, max_num + 1):
        # Get amount of nums lower than num at idx
        freq_list[idx] += freq_list[idx - 1]
        
    # Place the elements into sorted order
    for idx in range(len(nums) - 1, -1, -1):
        # Map the idx-last element in nums to its correct positon
        # Given that are i elements bigger the num then its pos is i+1
        # Subtraction by 1 cuz starts at zero
        sorted_list[freq_list[nums[idx]] - 1] = nums[idx]
        freq_list[nums[idx]] -= 1
        
    return sorted_list

        
#print(counting_sort([1,2,4,5,3,5,7,7,42,1]))