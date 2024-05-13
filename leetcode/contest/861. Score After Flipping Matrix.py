class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i] = [0 if x else 1 for x in grid[i]]


        cols = [0] * len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cols[c] += grid[r][c]
        
        for i in range(len(cols)):
            if cols[i] < len(grid) / 2:
                for r in range(len(grid)):
                    grid[r][i] = 0 if grid[r][i] else 1

        score = 0

        for r in grid:
            current = 0
            por = len(grid[0]) - 1
            for num in r:
                current += (2**por) * num
                por -= 1
            score += current

        return score
        