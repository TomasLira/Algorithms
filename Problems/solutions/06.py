import heapq

# Time complexity O(n log k)
def closest_elements(nums, target, k):
    heap = []
    # Remove biggest difference
    for i in range(len(nums)):
        difference = abs(target - nums[i])
        heapq.heappush(heap, (-difference, -nums[i]))
        if len(heap) > k:
            heapq.heappop(heap)
        
    result = [-heapq.heappop(heap)[1] for _ in range(k)]    
    return sorted(result)

print(closest_elements([1, 2, 36, 4, 6], 5, 3))



# Time complexity O(k log n)
def closest_elements(nums,target,k):
    heap = []
    for i in range(len(nums)):
        difference = abs(target-nums[i])
        heapq.heappush(heap,(difference,nums[i]))
    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[1])
    return result
    
print(closest_elements([1,2,36,4,6],5,3))
        

    
    