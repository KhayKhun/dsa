from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permu = defaultdict(int)
        for i in s1: permu[i] += 1
        l = 0

        while l < len(s2) - len(s1) + 1:
            target = s2[l:l+len(s1)]

            target_permu = defaultdict(int)
            for t in target: target_permu[t] += 1

            if target_permu == permu: return True
            # nope
            l += 1

        return False