from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        
        def findFarmlandCoordinates(row, col):
            coordinates = [row, col]
            r, c = row, col
            
            while r < len(land) and land[r][col] == 1:
                r += 1
            while c < len(land[0]) and land[row][c] == 1:
                c += 1
            
            coordinates.extend([r - 1, c - 1])
            
            for i in range(row, r):
                for j in range(col, c):
                    land[i][j] = 0
            
            return coordinates
        
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    result.append(findFarmlandCoordinates(i, j))
        
        return result
