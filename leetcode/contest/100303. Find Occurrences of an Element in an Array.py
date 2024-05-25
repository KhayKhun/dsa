class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        res = []
        xs = []
        for i, n in enumerate(nums):
            if n == x:
                xs.append(i)
        for q in queries:
            if q > len(xs):
                res.append(-1)
            else:
                res.append(xs[q-1])
        
        return res
        