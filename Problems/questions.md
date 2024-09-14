# Classic Algorithm Problems

# Algorithm Problems with Specific Time Complexities

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
