from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, target):
            # check if position is out of range. or word does not match target
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) or board[r][c] != word[target]:
                return False
            # board[r][c] matched and, is the last position of the word
            if target == len(word) - 1:
                return True
            
            # temporaly assign board[r][c] as '/'. Store the default value in temp.
            temp, board[r][c] = board[r][c], '/'
            found = dfs(r - 1, c, target + 1) or dfs(r + 1, c, target + 1) or dfs(r, c - 1, target + 1) or dfs(r, c + 1, target + 1)
            # not found? reassign to default value after the operations
            board[r][c] = temp

            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"

print(Solution().exist(board, word))
