class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        d[s[0]] += 1
        l,r = 0,1
        longest = 0

        while r < len(s):
            d[s[r]] += 1
            total = sum(d.values())
            others = total - max(d.values())
            
            # not violated
            if others <= k:
                longest = max(longest,total)
            # violated
            else:
                d[s[l]] -= 1
                l += 1
            r += 1
        
        return longest

        