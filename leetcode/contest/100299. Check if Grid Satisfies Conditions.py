from typing import List
from collections import defaultdict
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid[0])-1):
            if grid[0][i] == grid[0][i+1]: return False

        for i in range(len(grid)-1):
            if grid[i] != grid[i+1]: return False
        
        return True



print(Solution().satisfiesConditions([[1,0,2],[1,0,2]]))#t
print(Solution().satisfiesConditions([[1,1,1],[0,0,0]])) #f
print(Solution().satisfiesConditions([[1],[2],[3]])) #f
print(Solution().satisfiesConditions([[0]])) #t
print(Solution().satisfiesConditions([[1,4],[6,6]])) #f
print(Solution().satisfiesConditions([[6,6],[6,6]])) #f