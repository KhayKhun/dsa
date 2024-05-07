from typing import List
class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, v: int) -> None:
        for r in range(len(self.matrix)):
            if r < row1: continue
            if r > row2: break
            for c in range(len(self.matrix[0])):
                if c < col1 or c > col2: continue
                self.matrix[r][c] = v


    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)