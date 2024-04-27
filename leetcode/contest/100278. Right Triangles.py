from typing import List
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        count_based_on_rows = [0] * rows
        count_based_on_cols = [0] * cols
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count_based_on_rows[r] += 1
                    count_based_on_cols[c] += 1
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1: continue
                t = (count_based_on_rows[r] - 1) * (count_based_on_cols[c] - 1)
                count += t
                
        return count
    
grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]

print(Solution().numberOfRightTriangles(grid))