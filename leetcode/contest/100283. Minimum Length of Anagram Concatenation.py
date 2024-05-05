class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    def minAnagramLength(self, s: str) -> int:
        if not s: return 0
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        gcd_value = freq[s[0]]
        for key in freq:
            gcd_value = self.gcd(gcd_value, freq[key])
        
        return len(s) // gcd_value

# Example usage:
sol = Solution()

# Example 1
s1 = "abba"
print("Output:", sol.minAnagramLength(s1))  # Expected output: 2

# Example 2
s2 = "cdef"
print("Output:", sol.minAnagramLength(s2))  # Expected output: 4
