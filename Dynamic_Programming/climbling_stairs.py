from typing import List

# Poorly optimized function
def climbStairs1(n: int) -> int:
    if n == 2:
        return 2
    elif n == 1:
        return 1
    # if you're on step n-1, you can reach step n by taking one more step. The same logic for n-2
    return climbStairs1(n-1) + climbStairs1(n-2) 


# Uing memoization
def climbStairs2(n: int) -> int:
    def climbHelper(n, memo):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        elif n == 0:
            return 1
        memo[n] = climbHelper(n - 1, memo) + climbHelper(n - 2, memo)
        return memo[n]

    memo = {}
    return climbHelper(n, memo)

# Dynamic Programming
def climbStairs3(n: int) -> int:
    total,step1,step2, = 0,1,2
    for i  in range(2,n):
        total = step1 + step2
        step1 = step2
        step2 = total
    return total
      
print(climbStairs3(44))

