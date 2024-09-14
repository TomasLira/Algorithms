# Solution 1 O(n) Time
def top_k_frequent(nums,k):
    hash_table = {}
    # Get frequencies for each term in list 
    for num in nums:
        hash_table[num] = hash_table.get(num,0) + 1
    
    # Index of bucket associated with frequency
    buckets = [[] for _ in range(len(nums)+1)]
    
    for num,freq in hash_table.items():
        buckets[freq].append(num)
    result = []

    # get biggest frequency until k
    for bucket_idx in range(len(buckets)-1,-1,-1):
        for num in buckets[bucket_idx]:
            result.append(num)
        if len(result) == k:
            break
    return result


# Solution 2 O(n log k) Time
import heapq
def top_k_frequent(nums,k):
    hash_table = {}
    # Get frequencies for each term in list 
    for num in nums:
        hash_table[num] = hash_table.get(num,0) + 1
        
    min_heap = []
    for num,freq in hash_table.items():
        heapq.heappush(min_heap,(freq,num))
        # Keep track of the biggest k elements in heap, always removing the smaller node
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num for freq,num in min_heap] 