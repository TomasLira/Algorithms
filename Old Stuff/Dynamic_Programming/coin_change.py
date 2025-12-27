from typing import List
from collections import defaultdict
# Backtracking with memo
def coinChange(coins: List[int], amount: int) -> int:
        def coinHelper(amount,memo):
            if amount in memo:
                # Compares curr cost with a new cost being computed!
                return memo[amount]    
            elif amount == 0:
                return 0
            # init new cost for amount
            memo[amount] = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    #Levels of tree given by amount, num childs -> #coins 
                    # This garantees coin cost is 1! Draw the tree, memo gets updated
                    memo[amount] = min(memo[amount],coinHelper(amount - coin,memo)+1)
            return memo[amount]
        memo = {}
        res = coinHelper(amount,memo)
        return res if res != float("inf") else -1


# Dynamic Programming
def coinChange(coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for num in range(1, amount+1):
            for coin in coins:
                if num - coin >= 0:
                    # +1 for current coin, get dp of past vals and compares to prev vals of other coins
                    dp[num] = min(dp[num],dp[num-coin]+1)
        print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1
print(coinChange([2,3,5],7))
            
            
            



                    


