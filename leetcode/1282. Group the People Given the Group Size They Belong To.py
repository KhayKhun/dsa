from typing import List
class Solution:
    def groupThePeople(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        res = []
        for i in range(len(nums)):
            d[nums[i]].append(i)
        
        for key, val in d.items():
            i = 0
            for _ in range(len(val) // key):
                temp = []
                for _ in range(key):
                    temp.append(val[i])
                    i+=1
                res.append(temp)
        
        return res
        