from typing import List
from collections import defaultdict
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        count = 0
        d = defaultdict(list)
        maxi = float('inf')
        every = []
        for i in range(len(points)):
            far = max(abs(points[i][0]),abs(points[i][1]))
            every.append(far)
            d[s[i]].append(far)

        for key,val in d.items():
            if len(val) < 2: continue
            l = sorted(val,reverse=True)
            print(key, l)

            res = l.pop()
            if l:
                res = l.pop()
            
            maxi = min(maxi, res)

        for v in every:
            if v < maxi:
                count += 1
        return count

    
print(Solution().maxPointsInsideSquare([[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]],"abdca"))
print(Solution().maxPointsInsideSquare([[1,1],[-2,-2],[-2,2]],"abb"))
print(Solution().maxPointsInsideSquare([[1,1],[-1,-1],[2,-2]],"ccd"))
print(Solution().maxPointsInsideSquare([[16,32],[27,3],[23,-14],[-32,-16],[-3,26],[-14,33]],"aaabfc"))