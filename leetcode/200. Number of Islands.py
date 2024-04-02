class Solution:
    def numIslands(self, grid):
        row_count = len(grid)
        col_count = len(grid[0])

        land_count = 0

        for r in range(row_count):
            for c in range(col_count):
                if self.findLand(grid,r,c): land_count += 1

        return land_count

    def findLand(self, grid, r, c):
        if not (r >= 0 and r < len(grid)): return False
        if not (c >= 0 and c < len(grid[0])): return False
        if grid[r][c] != "1": return False

        grid[r][c] = '#'

        # expand
        self.findLand(grid,r + 1,c)
        self.findLand(grid,r - 1,c)
        self.findLand(grid,r,c + 1)
        self.findLand(grid,r,c - 1)

        return True

    
        