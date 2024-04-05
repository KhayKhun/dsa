# O(n^2), weird approach
class Solution:
    def makeGood(self, s: str) -> str:
        chance = 1
        while chance > 0:
            for i in range(len(s) - 1):
                if (s[i].upper() == s[i + 1].upper()) and s[i] != s[i+1]:
                    s = s[:i] + s[i+2:]
                    chance += 1
                    break
            chance -= 1
        return s
        
# O(n), stack apporach
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) and abs(ord(i) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)