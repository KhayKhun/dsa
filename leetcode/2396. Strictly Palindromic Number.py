# work hard
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n -1):
            if self.isPalindromic(self.getBase(n, i)) == False:
                return False
        
        return True

    def isPalindromic(self, s):
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return False

            l += 1
            r -= 1
        return True 

    def getBase(self, n: int, base: int) -> str:
        if n == 2: return bin(n)[2:]

        digits = ''
        while n:
            n, remainder = divmod(n, base)
            digits = str(remainder) + digits
        
        return digits

# work smart
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False