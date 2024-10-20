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

10. **Find Missing Positive Integer**
    - **Description**: Given a list `A` of `n` integers, some of which might be negative or zero, design an algorithm to find the smallest positive integer that is not present in `A`. The algorithm should have O(n) time complexity.
    - **Time Complexity**: O(n)

11. **Maximum Subarray Sum with No Adjacent Elements**
   - **Description**: Given an array `A` of `n` integers, design an algorithm to find the maximum sum of a subsequence where no two elements are adjacent. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)

12. **Smallest Subarray with Sum Greater than K**
   - **Description**: Given an array `A` of `n` positive integers and a positive integer `K`, design an algorithm to find the length of the smallest contiguous subarray whose sum is greater than `K`. The algorithm should have O(n) time complexity.
   - **Time Complexity**: O(n)

13. **Intersection of Two Arrays**
   - **Description**: Given two arrays `A` and `B` of sizes `m` and `n`, respectively, design an algorithm to find the intersection of `A` and `B` without duplicates. The algorithm should have O(m + n) time complexity.
   - **Time Complexity**: O(m + n)

14. **Closest Pair in Sorted Arrays**
   - **Description**: Given two sorted arrays `A` and `B`, design an algorithm to find the pair (one element from each array) with the smallest absolute difference. The algorithm should have O(m + n) time complexity.
   - **Time Complexity**: O(m + n)

15. **Longest Increasing Subsequence**
    - **Description**: Given an array `A` of `n` integers, design an algorithm to find the length of the longest increasing subsequence. The algorithm should have O(n log n) time complexity.
    - **Time Complexity**: O(n log n)

16. **Count Inversions in Array**
    - **Description**: Given an array `A` of `n` integers, design an algorithm to count the number of inversions in the array (where an inversion is a pair of indices `(i, j)` such that `i < j` and `A[i] > A[j]`). The algorithm should have O(n log n) time complexity.
    - **Time Complexity**: O(n log n)

17. **Find the Majority Element**
    - **Description**: Given an array `A` of `n` elements, design an algorithm to find the element that appears more than `n/2` times (if it exists). The algorithm should have O(n) time complexity.
    - **Time Complexity**: O(n)

18. **Find the Closest Value in BST**
    - **Description**: Given a binary search tree (BST) `T` and a target value `x`, design an algorithm to find the value in the BST that is closest to `x`. The algorithm should have O(log n) time complexity for balanced trees.
    - **Time Complexity**: O(log n)

19. **Maximum Profit from Stock Prices**
    - **Description**: Given an array `A` of `n` integers where each element represents the stock price on a given day, design an algorithm to find the maximum profit you can achieve by buying and selling once. The algorithm should have O(n) time complexity.
    - **Time Complexity**: O(n)

20. **Smallest Range Covering Elements from K Lists**
   - **Description**: Given `k` sorted lists, design an algorithm to find the smallest range that includes at least one element from each list. Use a combination of sorting, selection, and a greedy approach to efficiently find the smallest range.
   - **Time Complexity**: O(n log k), where `n` is the total number of elements across all lists.

21. **Find All Triplets with Zero Sum**
   - **Description**: Given a list `A` of `n` integers, design an algorithm to find all unique triplets `(i, j, k)` such that `A[i] + A[j] + A[k] = 0`. Use sorting and hashing to achieve this.
   - **Time Complexity**: O(n^2)

22. **Shortest Unsorted Subarray**
   - **Description**: Given a list `A` of `n` integers, design an algorithm to find the shortest continuous subarray such that sorting this subarray would make the entire list sorted. Use sorting and binary search to identify the subarray.
   - **Time Complexity**: O(n log n)

23. **Gas Station**
   - **Description**: You are given two arrays `gas` and `cost`, where `gas[i]` represents the amount of gas available at station `i` and `cost[i]` represents the cost of gas to travel to the next station. Design an algorithm to find the starting station from which you can travel around the circuit once if possible.
   - **Time Complexity**: O(n)

24. **Maximum Product of Three Numbers**
   - **Description**: Given a list `A` of `n` integers, design an algorithm to find the maximum product of any three numbers. Use a greedy strategy to determine the highest combination, considering both positive and negative values.
   - **Time Complexity**: O(n log n)

25. **Clone Graph**
   - **Description**: Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value and a list of its neighbors.
   - **Time Complexity**: O(N + E), where N is the number of nodes and E is the number of edges.

26. **Number of Islands**
   - **Description**: Given a 2D grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
   - **Time Complexity**: O(N * M), where N and M are the dimensions of the grid.

27. **Course Schedule**
   - **Description**: There are `numCourses` courses labeled from `0` to `numCourses-1`. Given prerequisites as pairs, determine if it's possible to finish all courses.
   - **Time Complexity**: O(N + E), where N is the number of courses and E is the number of prerequisites.

28. **Minimum Spanning Tree (Kruskal’s Algorithm)**
   - **Description**: Given a connected, undirected graph with weights, find the subset of edges that connects all vertices with the minimum total edge weight.
   - **Time Complexity**: O(E log E), where E is the number of edges.

29. **Word Ladder**
   - **Description**: Given two words, beginWord and endWord, and a word list, return the length of the shortest transformation sequence from beginWord to endWord, where only one letter can be changed at a time and each transformed word must exist in the word list.
   - **Time Complexity**: O(M * N), where M is the length of each word and N is the total number of words in the word list.

30. **Dijkstra's Shortest Path Algorithm**
   - **Description**: Given a graph and a source node, find the shortest path from the source node to all other nodes in the graph with non-negative weights.
   - **Time Complexity**: O((N + E) log N), where N is the number of nodes and E is the number of edges.

31. **Graph Valid Tree**
   - **Description**: Given n nodes labeled from `0` to `n-1` and a list of undirected edges, determine if these edges make up a valid tree.
   - **Time Complexity**: O(N + E), where N is the number of nodes and E is the number of edges.

32. **Redundant Connection**
   - **Description**: In a graph of `n` nodes, add one extra edge to ensure it remains a tree. Return the edge that can be removed while maintaining the tree structure.
   - **Time Complexity**: O(N), where N is the number of nodes.

33. **Critical Connections in a Network**
   - **Description**: Given a network of nodes and connections, find all the critical connections that, if removed, will cause the network to become disconnected.
   - **Time Complexity**: O(N + E), where N is the number of nodes and E is the number of edges.

34. **Longest Path in a Directed Acyclic Graph (DAG)**
   - **Description**: Given a directed acyclic graph, find the longest path from any vertex to any other vertex.
   - **Time Complexity**: O(N + E), where N is the number of nodes and E is the number of edges.

35. **Topological Sort**
   - **Description**: Given a directed graph, return a topological ordering of its vertices if one exists.
   - **Time Complexity**: O(N + E), where N is the number of nodes and E is the number of edges.

36. **All Paths from Source to Target**
   - **Description**: Given a directed acyclic graph, return all paths from the source node to the target node.
   - **Time Complexity**: O(2^N), where N is the number of nodes (in the worst case, you may need to explore every possible path).

37. **chromatic number of graphs**
   - **Description**: Give a linear algorithm to compute the chromatic number of graphs where each vertex has degree at most 2.
   - **Time Complexity**: O(N + E), where N is the number of node and E the number os edges


