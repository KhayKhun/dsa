class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ''
        for i in order:
            index = 0
            while index != -1:
                index = s.find(i)
                if index != -1: # exist
                    res += s[index]
                    s = s[:index] + s[index+1:]
        return res+s
    
    
order = "kqep"
s = "pekeq"
# "kqeep"

sol = Solution()
print(sol.customSortString(order, s))