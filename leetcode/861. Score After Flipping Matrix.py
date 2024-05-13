class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # flip rows
        for i in range(n):
            if grid[i][0] == 0:
                grid[i] = [0 if x else 1 for x in grid[i]]


        cols = [0] * m
        # count 1s
        for r in range(n):
            for c in range(m):
                cols[c] += grid[r][c]

        # flip the cols if count of 1s less than half
        for c in range(m):
            if cols[c] < n / 2:
                for r in range(n):
                    grid[r][c] = 0 if grid[r][c] else 1

        # calculate final binary result
        score = 0

        for r in grid:
            current = 0
            por = m - 1
            for num in r:
                current += (2**por) * num
                por -= 1
            score += current

        return score
