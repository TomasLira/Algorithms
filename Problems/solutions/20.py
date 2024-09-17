# Solution O(n^2) using dp
import bisect
def longest_sub(nums):
    dp = [1] * len(nums)
    max_length = 0
    for end in range(len(nums)):
        for start in range(end):
            if nums[end] > nums[start]:
                dp[end] = max(dp[end], dp[start] + 1)
        max_length = max(max_length, dp[end])
    return max_length

# Solution O(nlog(n)
def longest_sub(nums):
    dp = []
    for num in nums:
        # Use bs to find correct sorted pos in dp list
        pos = bisect.bisect_left(dp,num)
        if pos == len(dp):
            dp.append(num)
        else:
            dp[pos] = num
    return len(dp)
