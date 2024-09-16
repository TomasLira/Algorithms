# Classic Algorithm Problems

1. **Top K Frequent Elements**
   - **Description**: Given an integer `k` and a list `A` of integers containing `n` elements with `m` distinct numbers (where `m ≥ k`), design an algorithm to return the `k` most frequent integers in the list. The algorithm should have O(n) time complexity in the worst case.
   - **Time Complexity**: O(n)

2. **Pair Sum**
   - **Description**: Given an integer `x` and a list `A` containing `n` integers, design an algorithm to find a pair of integers in `A` whose sum equals `x`, if such a pair exists. The algorithm should have O(n) time complexity in the worst case.
   - **Time Complexity**: O(n)

3. **Lists with Unique Elements**
   - **Description**: Given a list `A` containing `n` lists with `m` integers each, design an algorithm to return the number of lists that do not share any elements with any other list. The algorithm should have O(n * m) time complexity in the worst case.
   - **Time Complexity**: O(n * m)

4. **Largest Integer with Sufficient Count**
   - **Description**: Given a list `A` of `n` non-negative integers, design an algorithm to return the largest integer `x` in `A` such that there are at least `x` integers in `A` that are greater than or equal to `x` (including `x` itself), or -1 if no such integer exists. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)

5. **Minimum Difference in BST**
   - **Description**: Given a binary search tree (BST) `T` with `n` nodes containing integers, design an algorithm to find the minimum absolute difference between the values of any two distinct nodes in the tree. The algorithm should have O(n) time complexity in the worst case.
   - **Time Complexity**: O(n)

6. **K Closest Elements**
   - **Description**: Given two integers `x` and `k`, and a list `A` containing `n` integers, design an algorithm to return the `k` elements from `A` that are closest to `x`, in ascending order of their proximity. The algorithm should have O(n log k) time complexity in the worst case.
   - **Time Complexity**: O(n log k)

7. **Largest Subarray with Limited Difference**
   - **Description**: Given a positive integer `x` and a list `A` containing `n` integers, design an algorithm to return the largest subarray from `A` such that the maximum difference between any two elements in the subarray is at most `x`. The algorithm should have O(n log n) time complexity in the worst case.
   - **Time Complexity**: O(n log n)

8. **Maximum Product of Distance and Minimum Value**
   - **Description**: Given a list `A` of `n` integers, design a greedy algorithm to find the pair of indices `(i, j)` such that the product `|i - j| * min{A[i], A[j]}` is maximized. The algorithm should have O(n) time complexity in the worst case.
   - **Time Complexity**: O(n)

9. **Balanced BST Construction**
   - **Description**: Given a list `A` of `n` integers, design a divide-and-conquer algorithm to build a balanced binary search tree (BST) containing all the elements of `A`. The algorithm should have O(n log n) time complexity in the worst case.
   - **Time Complexity**: O(n log n)

10. **Find Missing Positive Integer**
    - **Description**: Given a list `A` of `n` integers, some of which might be negative or zero, design an algorithm to find the smallest positive integer that is not present in `A`. The algorithm should have O(n) time complexity.
    - **Time Complexity**: O(n)



11. **Median of Two Sorted Arrays**
   - **Description**: Given two sorted arrays `A` and `B` of sizes `m` and `n`, respectively, design an algorithm to find the median of the combined sorted array. The algorithm should have O(log(min(m, n))) time complexity.
   - **Time Complexity**: O(log(min(m, n)))

12. **Longest Substring with At Most K Distinct Characters**
   - **Description**: Given a string `S` and an integer `k`, design an algorithm to find the length of the longest substring with at most `k` distinct characters. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)

13. **Find All Anagrams in a String**
   - **Description**: Given a string `S` and a pattern `P`, design an algorithm to find all starting indices of `P`'s anagrams in `S`. The algorithm should have O(n) time complexity, where `n` is the length of `S`.
   - **Time Complexity**: O(n)

14. **Maximum Subarray Sum with No Adjacent Elements**
   - **Description**: Given an array `A` of `n` integers, design an algorithm to find the maximum sum of a subsequence where no two elements are adjacent. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)

15. **Find Duplicate Number**
   - **Description**: Given an array `A` of `n+1` integers where each integer is between `1` and `n`, design an algorithm to find the duplicate number. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)

16. **Smallest Subarray with Sum Greater than K**
   - **Description**: Given an array `A` of `n` positive integers and a positive integer `K`, design an algorithm to find the length of the smallest contiguous subarray whose sum is greater than `K`. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)

17. **Intersection of Two Arrays**
   - **Description**: Given two arrays `A` and `B` of sizes `m` and `n`, respectively, design an algorithm to find the intersection of `A` and `B` without duplicates. The algorithm should have O(m + n) time complexity.
   - **Time Complexity**: O(m + n)

18. **Find the Missing Number**
   - **Description**: Given an array `A` containing `n` distinct numbers from `0` to `n`, design an algorithm to find the missing number in the array. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)

19. **Closest Pair in Sorted Arrays**
   - **Description**: Given two sorted arrays `A` and `B`, design an algorithm to find the pair (one element from each array) with the smallest absolute difference. The algorithm should have O(m + n) time complexity.
   - **Time Complexity**: O(m + n)

20. **Longest Increasing Subsequence**
    - **Description**: Given an array `A` of `n` integers, design an algorithm to find the length of the longest increasing subsequence. The algorithm should have O(n log n) time complexity.
    - **Time Complexity**: O(n log n)

21. **Rotate Matrix**
    - **Description**: Given an `n x n` matrix, design an algorithm to rotate the matrix 90 degrees clockwise in place. The algorithm should have O(n^2) time complexity.
    - **Time Complexity**: O(n^2)

22. **Count Inversions in Array**
    - **Description**: Given an array `A` of `n` integers, design an algorithm to count the number of inversions in the array (where an inversion is a pair of indices `(i, j)` such that `i < j` and `A[i] > A[j]`). The algorithm should have O(n log n) time complexity.
    - **Time Complexity**: O(n log n)

23. **Find the Majority Element**
    - **Description**: Given an array `A` of `n` elements, design an algorithm to find the element that appears more than `n/2` times (if it exists). The algorithm should have O(n) time complexity.
    - **Time Complexity**: O(n)

24. **Find the Closest Value in BST**
    - **Description**: Given a binary search tree (BST) `T` and a target value `x`, design an algorithm to find the value in the BST that is closest to `x`. The algorithm should have O(log n) time complexity for balanced trees.
    - **Time Complexity**: O(log n)

25. **Maximum Profit from Stock Prices**
    - **Description**: Given an array `A` of `n` integers where each element represents the stock price on a given day, design an algorithm to find the maximum profit you can achieve by buying and selling once. The algorithm should have O(n) time complexity.
    - **Time Complexity**: O(n)


26. **Minimum Platforms Required**
   - **Description**: Given two lists `arrival` and `departure`, representing the arrival and departure times of trains, design an algorithm to find the minimum number of platforms required at the station so that no train waits. The algorithm should use a greedy approach combined with sorting and searching.
   - **Time Complexity**: O(n log n)

27. **Largest Rectangle in Histogram**
   - **Description**: Given a list `A` of `n` non-negative integers representing the heights of a histogram, design an algorithm to find the largest rectangle that can be formed within the histogram. Use a stack-based greedy approach combined with searching.
   - **Time Complexity**: O(n)



28. **Smallest Range Covering Elements from K Lists**
   - **Description**: Given `k` sorted lists, design an algorithm to find the smallest range that includes at least one element from each list. Use a combination of sorting, selection, and a greedy approach to efficiently find the smallest range.
   - **Time Complexity**: O(n log k), where `n` is the total number of elements across all lists.


29. **Divide Array into K Subarrays with Minimum Largest Sum**
   - **Description**: Given a list `A` of `n` integers and an integer `k`, design an algorithm to divide the array into `k` contiguous subarrays such that the maximum sum of any subarray is minimized. Use a combination of binary search and greedy strategies.
   - **Time Complexity**: O(n log S), where `S` is the sum of all elements in `A`.



30. **Find All Triplets with Zero Sum**
   - **Description**: Given a list `A` of `n` integers, design an algorithm to find all unique triplets `(i, j, k)` such that `A[i] + A[j] + A[k] = 0`. Use sorting and hashing to achieve this.
   - **Time Complexity**: O(n^2)

31. **K-th Largest Element in a Stream**
   - **Description**: Given a stream of integers and an integer `k`, design an algorithm to find the `k`-th largest element in the stream at any point in time. Use a combination of a min-heap (priority queue) and selection.
   - **Time Complexity**: O(n log k)

32. **Maximize Sum After K Negations**
   - **Description**: Given a list `A` of `n` integers, design an algorithm to maximize the sum of the array after performing at most `k` negations (negate any element by multiplying it by `-1`). Use a greedy strategy combined with sorting.
   - **Time Complexity**: O(n log n)

33. **Merge Intervals with Maximum Overlap**
   - **Description**: Given a list of intervals, design an algorithm to merge all overlapping intervals while maximizing the total overlap. Use sorting combined with greedy strategies to efficiently find and merge the intervals.
   - **Time Complexity**: O(n log n)

34. **Shortest Unsorted Subarray**
   - **Description**: Given a list `A` of `n` integers, design an algorithm to find the shortest continuous subarray such that sorting this subarray would make the entire list sorted. Use sorting and binary search to identify the subarray.
   - **Time Complexity**: O(n log n)

35. **Find the Median in a Data Stream**
   - **Description**: Given a stream of integers, design an algorithm to continuously return the median of the elements processed so far. Use a combination of two heaps (max-heap and min-heap) to maintain the median in O(log n) time for each insertion.
   - **Time Complexity**: O(n log n)

36. **Fibonacci Number**
   - **Description**: Given an integer `n`, design an algorithm to return the `n`th Fibonacci number. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)


37. **Climbing Stairs**
   - **Description**: Given an integer `n`, representing the number of steps, design an algorithm to determine how many distinct ways you can climb to the top. You can climb either 1 step or 2 steps at a time. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)


38. **House Robber**
   - **Description**: Given an array `A` of `n` non-negative integers representing the amount of money in each house, design an algorithm to determine the maximum amount of money you can rob without alerting the police (you cannot rob two adjacent houses). The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)


39. **Min Cost Climbing Stairs**
   - **Description**: Given an array `A` of `n` integers where `A[i]` is the cost of stepping on the `i`th step, design an algorithm to determine the minimum cost to reach the top of the staircase. You can either start from the 0th or 1st step. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)


40. **Coin Change**
   - **Description**: Given an array `A` representing available coin denominations and an integer `x`, design an algorithm to determine the minimum number of coins needed to make up the amount `x`. The algorithm should have O(x * n) time complexity.
   - **Time Complexity**: O(x * n)


41. **Longest Common Subsequence**
   - **Description**: Given two strings `A` and `B`, design an algorithm to find the length of their longest common subsequence. The algorithm should have O(n * m) time complexity, where `n` and `m` are the lengths of `A` and `B`, respectively.
   - **Time Complexity**: O(n * m)


42. **Partition Equal Subset Sum**
   - **Description**: Given an array `A` of `n` integers, design an algorithm to determine whether you can partition the array into two subsets such that the sum of both subsets is equal. The algorithm should have O(n * S) time complexity, where `S` is half the total sum of `A`.
   - **Time Complexity**: O(n * S)


43. **Edit Distance**
   - **Description**: Given two strings `A` and `B`, design an algorithm to find the minimum number of operations (insertions, deletions, or substitutions) required to convert `A` into `B`. The algorithm should have O(n * m) time complexity, where `n` and `m` are the lengths of `A` and `B`, respectively.
   - **Time Complexity**: O(n * m)


44. **Maximum Subarray Sum**
   - **Description**: Given an array `A` of `n` integers, design an algorithm to find the contiguous subarray with the maximum sum. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)


45. **Unique Paths**
    - **Description**: Given two integers `m` and `n`, representing a grid of size `m x n`, design an algorithm to find how many unique paths exist from the top-left corner to the bottom-right corner, moving only right or down. The algorithm should have O(m * n) time complexity.
    - **Time Complexity**: O(m * n)


46. **Triangle Minimum Path Sum**
    - **Description**: Given a triangle of integers, where each row contains one more element than the previous row, design an algorithm to find the minimum path sum from the top to the bottom. You can only move to adjacent numbers in the next row. The algorithm should have O(n^2) time complexity.
    - **Time Complexity**: O(n^2)


47. **Word Break**
   - **Description**: Given a string `S` and a dictionary `D` of words, design an algorithm to determine if `S` can be segmented into a space-separated sequence of one or more dictionary words. The algorithm should have O(n^2) time complexity, where `n` is the length of the string.
   - **Time Complexity**: O(n^2)


48. **Palindromic Substrings**
   - **Description**: Given a string `S`, design an algorithm to find how many palindromic substrings are present in `S`. The algorithm should have O(n^2) time complexity.
   - **Time Complexity**: O(n^2)


49. **Longest Palindromic Subsequence**
   - **Description**: Given a string `S`, design an algorithm to find the length of the longest palindromic subsequence in `S`. The algorithm should have O(n^2) time complexity.
   - **Time Complexity**: O(n^2)


50. **Decode Ways**
   - **Description**: Given a string `S` containing only digits, design an algorithm to determine how many ways the string can be decoded, assuming `1` maps to `A`, `2` maps to `B`, and so on up to `26`. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)
