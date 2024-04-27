from typing import List
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        xs = [[0,0,1,1],[1,1,2,2]]
        ys = [[0,1,0,1],[1,2,1,2]]

        def explore(x,y):
            black = 0
            white = 0

            for a,b in zip(x,y):
                if grid[a][b] == 'B': black += 1
                else: white += 1
            if black >= 3 or white >= 3: return True

            return False

        for x in xs:
            for y in ys:
                if explore(x,y): return True
        return False

grid =  [["B","W","B"],["B","W","W"],["B","W","W"]]
print(Solution().canMakeSquare(grid))