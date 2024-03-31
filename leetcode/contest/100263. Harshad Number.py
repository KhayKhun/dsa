class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        chi = 0
        for i in s:
            chi += int(i)
        
        return chi if x % chi == 0 else -1
        
print(Solution().sumOfTheDigitsOfHarshadNumber(2))