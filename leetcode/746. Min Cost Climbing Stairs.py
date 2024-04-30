from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def explore(i):
            if i in memo: return memo[i]
            if i >= len(cost): return 0
            
            memo[i] = cost[i] + min(explore(i + 1), explore(i + 2))
            return memo[i]
        
        return min(explore(0), explore(1))

