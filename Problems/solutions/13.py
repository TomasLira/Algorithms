# Solution O(n+m)
def intersection(nums1,nums2):
    set1, set2 = set(nums1), set(nums2)
    return list(set1.intersection(set2))