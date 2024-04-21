class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        s = set(word)
        for c in s:
            if  c.lower() in s and c.upper() in s:
                count+=1
        return count//2
        