class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}

        for i in range(len(s)):
            if s[i] in d:
                if abs(i - d[s[i]] - 1) != distance[ord(s[i]) - 97]:
                    return False
            else:
                d[s[i]] = i

        return True