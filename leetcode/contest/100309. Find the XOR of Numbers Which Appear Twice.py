class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s = set()
        t = []
        for n in nums:
            if n in s:
                t.append(n)
            else:
                s.add(n)
         
        return reduce(lambda x, y: x ^ y, t) if len(t) > 0 else 0