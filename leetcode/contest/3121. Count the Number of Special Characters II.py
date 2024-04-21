from collections import defaultdict
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d = defaultdict(list)
        count = 0
        for i in word:
            d[i.lower()].append(ord(i))

        for val in d.values():
            if len(val) >= 2 and val[0] - val[-1] == 32:
                isValid = True
                for i in range(len(val)-1):
                    if val[i] < val[i+1]:
                        isValid = False
                        break
                if isValid: count += 1
        return count