from collections import defaultdict, Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l,r = 0,0
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

# Time Complexity :  O(n)
# Space Complexity : O(1)
class Solution(object):
    def characterReplacement(self, s, k):
        maxlen, largestCount = 0, 0
        arr = Counter()
        for idx in range(len(s)):
            arr[s[idx]] += 1
            largestCount = max(largestCount, arr[s[idx]])
            if maxlen - largestCount >= k:
                arr[s[idx - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen