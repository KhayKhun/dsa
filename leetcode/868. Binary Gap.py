class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)
        m = 0
        l,r = 2,3

        while r<len(s):
            if s[r] == '1':
                m = max(m, r-l)
                l = r
            r+=1

        return m
        