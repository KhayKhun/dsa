class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        drunk = 0
        while numBottles > 0 or emptyBottles >= numExchange:
            if emptyBottles >= numExchange:
                numBottles += 1
                emptyBottles -= numExchange
                numExchange += 1
            else:
                drunk += numBottles
                emptyBottles += numBottles
                numBottles = 0

        return drunk
    

numBottles = 10
numExchange = 3
print(Solution().maxBottlesDrunk(numBottles,numExchange))