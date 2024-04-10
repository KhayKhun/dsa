class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s,d = s.split(), dict()

        # important! 
        if len(s) != len(pattern): return False
        if len(set(s)) != len(set(pattern)): return False
        # important! 

        for i in range(len(s)):
            word = s[i]
            key = pattern[i]
            if not key in d:
                d[key] = word
            else:
                if d[key] != word:
                    return False
        return True
