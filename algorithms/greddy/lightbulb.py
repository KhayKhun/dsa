# bulbs = List[int] of {0, 1}
# 1 = lighted
# 0 = offed
# +1 cost everytime we turn on a bulb
# all bulbs from right side will be flipped
# O (n)
from typing import List
class Solution:
    def minimun_cost_to_light_all_bulbs(self,bulbs : List[int]) -> int:
        cost = 0

        for b in bulbs:
            # cost is odd
            if cost % 2 == 1: b = not b

            # b is 0
            if b % 2 == 0: cost += 1
        return cost

print(Solution().minimun_cost_to_light_all_bulbs([1,0,1]))
