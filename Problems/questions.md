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

38. **Construct BST**
   - **Description**: Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
   - **Time Complexity**: O(N), where N is the number of node

39. **Square of directed Graph**
   - **Description**: The square of a directed graph G = (V, E) is the graph G2 = (V, E2) such that (u,w) ∈ E2 iff there exists v ∈ V such that (u,v) ∈ E and (v,w) ∈ E; i.e., there is a path of exactly two edges from u to w.
   - **Time Complexity**: O(V*E), where V is the number of node and E the number of edges

40. **Rotting Oranges**
   - **Description**: You are given an m x n grid where each cell can have one of three values:  
   - `0` representing an empty cell,  
   - `1` representing a fresh orange,  
   - `2` representing a rotten orange.  
   Every minute, any fresh orange that is 4-directionally adjacent (up, down, left, right) to a rotten orange becomes rotten.  
   Return the minimum number of minutes that must elapse until no cell has a fresh orange. If it is impossible to rot all the fresh oranges, return `-1`.
   - **Time Complexity**: O(m * n), where m is the number of rows and n is the number of columns in the grid.

41. **Find the Ordering of Tasks from Given Dependencies (Course Schedule II)**
   - **Description**: You are given `N` tasks labeled from `0` to `N-1`, and a list of prerequisite pairs where each pair `[a, b]` indicates that task `a` depends on task `b` (i.e., you must finish task `b` before task `a`). Your goal is to determine a valid ordering of tasks such that all tasks can be completed, respecting their dependencies. If it is impossible to complete all tasks due to a cycle in the dependency graph, return an empty array. If there are multiple valid orderings, return any one of them.
   - **Time Complexity**: O(N + E), where `N` is the number of tasks and `E` is the number of prerequisite pairs (edges). This complexity comes from performing a topological sort of the dependency graph.


42. **Check Whether a Given Graph is Bipartite or Not**
   - **Description**:  
   Given an adjacency list representing an undirected graph with `V` vertices indexed from `0` to `V-1`, determine whether the graph is **bipartite** or not. A graph is considered bipartite if you can divide its set of vertices into two disjoint sets such that no two adjacent vertices share the same set. A graph is bipartite if and only if it is possible to color the graph using two colors in such a way that no two adjacent vertices have the same color.
   - **Time Complexity**:  
   O(V + E), where `V` is the number of vertices and `E` is the number of edges in the graph. This is the time complexity for performing a BFS or DFS traversal to check for bipartiteness.

43. **Path with Maximum Probability**
   - **Description**:  
   You are given an undirected weighted graph with `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a, b]` is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing that edge `succProb[i]`. Given two nodes, `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability.If there is no path from `start` to `end`, return `0`.
   - **Time Complexity**:  
  O(E log V), where `V` is the number of vertices and `E` is the number of edges in the graph.

44. **Cheapest Flights Within K Stops**
   - **Description**:  
   There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`. You are also given three integers: `src`, `dst`, and `k`. Your task is to return the cheapest price from city `src` to city `dst` with at most `k` stops. If there is no such route, return `-1`.
   - **Time Complexity**:  
  O(K * E), where `K` is the maximum number of stops and `E` is the number of edges in the flight list.

45. **Shortest Path Through Specified Vertices in Order**
   - **Description**:  
     Given a strongly connected directed graph without weights and a list `L` of vertices in the graph, return the shortest path that passes through all vertices in `L` in the specified order. The graph is represented as an adjacency list, and the list `L` contains vertices that must be visited in sequence.
   - **Time Complexity**:  
      O(len(L)(V + E)), where `V` is the number of vertices, `E` is the number of edges in the graph, and `len(L)` is the number of vertices in the list `L`.

46. **Vertex with Minimum Maximum Distance**
   - **Description**:  
     Given a strongly connected directed graph with weights and a list `L` of vertices in the graph, return the vertex `V` such that the maximum distance from any vertex in `L` to `V` is minimized. In other words, find the vertex `V` that minimizes `max{d(L[0], V), d(L[1], V), ..., d(L[N-1], V)}`, where `d(u, v)` represents the shortest distance from `u` to `v`.
   - **Time Complexity**:  
   The time complexity is O(N (V log V + E)), where `N` is the number of vertices in `L`, `V` is the total number of vertices, and `E` is the number of edges in the graph.

47. **Cheapest Path with Distance Constraint**
   - **Description**:  
     Given a directed graph with weighted edges, a path `C`, and a positive integer `X`, design an algorithm to find the cheapest path `C'` that starts and ends at the same vertices as `C`. The constraint is that the distance from any vertex in `C'` to its nearest vertex in `C` must not exceed `X`.
   - **Time Complexity**:  
    O(V log V + E), where `V` is the number of vertices and `E` is the number of edges

48. **Minimum Cost to Connect All Points**  
- **Description**:  
  You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`. The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`. Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.  
- **Time Complexity**:  
  Depends on the algorithm used (e.g., Kruskal's or Prim's algorithm).

49. **Number of Provinces**  
- **Description**:  
  There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`. A **province** is a group of directly or indirectly connected cities and no other cities outside of the group. You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i`th city and the `j`th city are directly connected, and `isConnected[i][j] = 0` otherwise. Return the total number of provinces.  
- **Time Complexity**:  
  O(n²) for a DFS or BFS approach.

50. **Connected Components: Weakly or Strongly Connected?**
   - **Description**:  
   Given a directed graph with `V` vertices and `E` edges, determine whether the graph is weakly or strongly connected. A graph is **strongly connected** if every vertex is reachable from every other vertex via directed paths. It is **weakly connected** if replacing all directed edges with undirected ones results in a connected graph.  
   - **Time Complexity**:  
   O(V + E), using Kosaraju's or Tarjan's algorithm to identify strongly connected components.

51. **Tree Identification**
   - **Description**:  
   Given an undirected graph, determine whether it is a tree. A graph is a tree if it is connected and contains no cycles.  
   - **Time Complexity**:  
   O(V + E), by performing a DFS or BFS to check for cycles and connectivity.

52. **Is Your Graph a Directed Acyclic Graph (DAG)?**
   - **Description**:  
   Determine whether a directed graph is acyclic. If the graph is a DAG, compute the shortest path from a given source `s` to all vertices using a topological sort. Shortest path is calculated as:  
   $$
   d(s, j) = \min_{(i, j) \in E} \{ d(s, i) + w(i, j) \}
   $$
   Use the same approach (replacing `min` with `max`) to find the longest path in a DAG.  
   - **Time Complexity**:  
   O(V + E) for topological sorting and path calculation.

53. **Shortest Cycle in a Graph**
   - **Description**:  
   Find the shortest cycle (or **girth**) in an undirected or directed graph. Use all-pairs shortest path algorithms (e.g., Floyd-Warshall) to compute cycles by identifying paths that return to the starting vertex.  
   - **Time Complexity**:  
   O(V³) using Floyd-Warshall or O(V * (V + E)) with BFS for each vertex in unweighted graphs.


54. Maximum Increase in Minimum Spanning Tree Cost
- **Description**:  
  Given a connected, undirected graph with weighted edges, identify the edge whose removal would cause the largest increase in the cost of the minimum spanning tree (MST).

- **Time Complexity**:  
  Depends on the approach:  
  - **O(E log V)** for constructing the MST (e.g., using Kruskal's or Prim's algorithm).  
  - Additional complexity to evaluate the impact of edge removal.

55. Algorithms to Filter Vertices Based on Tree Properties

- **Description**:  
  Given a graph G = (V, E), a rooted tree  T derived from G, and a list  L_1 containing vertices of the tree:  
  Write three algorithms that return a list L_2, containing vertices such that a vertex is in  L_2 if and only if it is in L_1 or:  
  - (a) Has an odd number of descendants in L_2.  
  - (b) Has an odd number of ancestors in L_2 .  
  - (c) Has an odd number of older siblings in  L_2.  

- **Time Complexity**:  
  Dependent on the tree traversal and list update methods. For efficient solutions:  
  - **O(V + E)** with a single DFS for computing descendants, ancestors, or siblings.