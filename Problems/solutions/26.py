import random

#Solution 1 Time O(n)
def min_platforms_correct(arrival, departure):
    platform_num = 1
    max_platforms = 1
    
    i,j = 1,0
    
    while i < len(arrival) and j < len(arrival):
        if arrival[i] <= departure[j]:
            platform_num += 1
            i +=1
        else:
            platform_num -= 1
            j += 1
        max_platforms = max(max_platforms,platform_num)
    return max_platforms    

# Wrong implementation edge cases
def min_platforms_user(arrival, derp):
    intervals_list = []
    min_interval = [arrival[0], derp[0]]
    counter, max_val = 1, 1
    for i in range(len(arrival)):
        intervals_list.append([arrival[i], derp[i]])

    for list_idx in range(1, len(intervals_list)):
        if intervals_list[list_idx][0] > min_interval[1]:
            min_interval = [intervals_list[list_idx][0], intervals_list[list_idx][1]]
            counter = 1
        else:
            min_interval[0] = max(intervals_list[list_idx][0], min_interval[0])
            min_interval[1] = min(intervals_list[list_idx][1], min_interval[1])
            counter += 1
        max_val = max(counter, max_val)
    return max_val