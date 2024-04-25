from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [None] * n
        
        def explore(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(explore(i + 1), explore(i + 2))
            return memo[i]
        
        return min(explore(0), explore(1))


cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution().minCostClimbingStairs(cost))