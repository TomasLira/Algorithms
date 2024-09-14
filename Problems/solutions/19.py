# Solution 1 O(n) Time
def closest_pair(l1, l2):
    idx1, idx2 = 0, 0
    min_diff = float('inf')
    
    while idx1 < len(l1) and idx2 < len(l2):
        min_diff = min(abs(l1[idx1] - l2[idx2]), min_diff)        
        if l1[idx1] < l2[idx2]:
            idx1 += 1
        elif l2[idx2] < l1[idx1]:
            idx2 += 1
        else: 
            return 0
    return min_diff

print(closest_pair([1, 4, 9, 13], [5, 8, 10]))

# Solution 2 O(n) Time
    