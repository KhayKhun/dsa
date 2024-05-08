from typing import List
class Solution:
    memo = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in self.memo: return self.memo[s]
        if s == "": return True
        for w in wordDict:
            if w in s and s.index(w) == 0:
                n = s[len(w):]
                if self.wordBreak(n, wordDict):
                    self.memo[n] = True
                    return True
        
        self.memo[s] = False
        return False

print(Solution().wordBreak("aaaaaaa",["aaaa","aaa"]))