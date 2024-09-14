import random

def randomized_partition(array, start, end):
    random_index = random.randint(start, end)  
    array[random_index], array[end] = array[end], array[random_index]  # Swap pivot to last pos
    return partition(array, start, end)

# Same logic as quicksort partition
def partition(array, start, end):
    pivot = array[end]
    smaller_index = start - 1
    for current_index in range(start, end):
        if array[current_index] <= pivot:
            smaller_index += 1
            # smaller idx always points to an element bigger than pivot and swaps with a smaller one.
            array[smaller_index], array[current_index] = array[current_index], array[smaller_index]
    array[smaller_index + 1], array[end] = array[end], array[smaller_index + 1]
    return smaller_index + 1

def randomized_select(array, start, end, target_order):
    if start == end:
        return array[start]
    
    pivot_index = randomized_partition(array, start, end)
    relative_order = pivot_index - start + 1
    if target_order == relative_order:
        return array[pivot_index]
    # Discard half of values
    # Analyzing the relative_order +- i = target_order
    elif target_order < relative_order:
        return randomized_select(array, start, pivot_index - 1, target_order)
    else:
        return randomized_select(array, pivot_index + 1, end, target_order - relative_order)


array = [1,2,2,3,4,5,5,6,7]
target_order = len(array)//2 
result = randomized_select(array, 0, len(array) - 1,target_order)
print(f"The {target_order}th smallest element is: {result}")
