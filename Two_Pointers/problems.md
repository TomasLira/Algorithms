# Problems

## Pair Sum – Sorted

Given an array of integers sorted in ascending order and a target value, return the indices of any pair of numbers in the array whose sum equals the target.

- The order of the indices in the result does not matter.
- If no such pair exists, return an empty array.

---

### Example 1

**Input:**  
nums = [-5, -2, 3, 4, 6], target = 7  

**Output:**  
[2, 3]

**Explanation:**  
nums[2] + nums[3] = 3 + 4 = 7

---

### Example 2

**Input:**  
nums = [1, 1, 1], target = 2  

**Output:**  
[0, 1]

**Explanation:**  
Other valid outputs include [1, 0], [0, 2], [2, 0], [1, 2], or [2, 1].

---

## Triplet Sum

Given an array of integers, return all triplets [a, b, c] such that  
$a + b + c = 0$.

- The solution must not contain duplicate triplets  
  (e.g. $[1, 2, 3]$ and $[2, 3, 1]$ are considered duplicates).
- If no such triplets are found, return an empty array.
- Each triplet can be arranged in any order.
- The output can be returned in any order.

---

### Example

**Input:**  
nums = [0, -1, 2, -3, 1]

**Output:**  
[[-3, 1, 2], [-1, 0, 1]]
