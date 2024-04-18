from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        def isWater(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]): return True
            return grid[r][c] == 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 1:
                    continue
                
                if isWater(r + 1,c): count += 1
                if isWater(r - 1,c): count += 1
                if isWater(r,c + 1): count += 1
                if isWater(r,c - 1): count += 1
        return count
            
        