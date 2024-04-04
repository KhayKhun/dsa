from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        l,r = 0,0
        max_length = 0

        while r < len(s):
            d[s[r]] += 1

            isDupli = False
            for i in d.values():
                if i > 1: 
                    isDupli = True
                    break

            if not isDupli:
                size = 0
                for i in d.values():
                    if i: size += 1
                max_length = max(max_length,size)
            else:
                d[s[l]] -= 1
                l += 1
            r += 1

        return max_length
    
# other

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length