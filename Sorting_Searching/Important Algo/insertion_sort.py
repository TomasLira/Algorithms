from typing import List
from functools import reduce

#Iterative:
def insertion_sort(nums:List[int])-> List[int]:
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
    return nums

#Recursive:
def insert(x, sorted_list):
    if not sorted_list or x <= sorted_list[0]:
        return [x] + sorted_list
    else:
        return [sorted_list[0]] + insert(x, sorted_list[1:])

def insertion_sort_rec(nums: List[int]):
    # Initialized [] to sorted_list and then applied insert operation on it with a new element 
    return reduce(lambda sorted_list,elem:insert(elem,sorted_list) ,nums,[])

# insert(4, []) -> [4]
# insert(2, [4]) -> [2, 4]
# insert(7, [2, 4]) -> [2, 4, 7]
# insert(1, [2, 4, 7]) -> [1, 2, 4, 7]
# insert(3, [1, 2, 4, 7]) -> [1, 2, 3, 4, 7]
# Output: [1, 2, 3, 4, 7]


a = [[1,2,3,4],[4,5,6,6,],[7,8,9,1]]
print(len(a[1]))

