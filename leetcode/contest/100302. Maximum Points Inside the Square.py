from typing import List
from collections import defaultdict
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        count = 0
        d = {}
        maxi = float('inf')
        every = []
        for i in range(len(points)):
            far = max(abs(points[i][0]),abs(points[i][1]))
            every.append(far)

            if s[i] not in d:
                d[s[i]] = far
            else:
                prev = d[s[i]]
                current = points[i]

                d[s[i]] = max(prev,abs(current[0]),abs(current[1]))
                maxi = min(maxi, d[s[i]])

        for v in every:
            if v < maxi:
                count += 1
        print(every, maxi)
        return count

    
# print(Solution().maxPointsInsideSquare([[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]],"abdca"))
# print(Solution().maxPointsInsideSquare([[1,1],[-2,-2],[-2,2]],"abb"))
# print(Solution().maxPointsInsideSquare([[1,1],[-1,-1],[2,-2]],"ccd"))
print(Solution().maxPointsInsideSquare([[16,32],[27,3],[23,-14],[-32,-16],[-3,26],[-14,33]],"aaabfc"))