class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
            'O': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = 'O'
        res = 0
        for i in range(len(s)-1, -1, -1):
            res += data[s[i]] if data[prev] <= data[s[i]] else -data[s[i]]
            prev = s[i]
        return res
        