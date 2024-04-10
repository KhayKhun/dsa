from typing import List
from math import *
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        x = len(deck) % 2 # even, odd = 0, 1
        res = [None for _ in range(len(deck))]
        r = 0
        for i in range(len(deck)):
            index = i * 2
            if index < len(deck):
                res[index] = deck[i]
            else:
                index = index + x
                x += 2
        return [1]
        
print(Solution().deckRevealedIncreasing([1,2,3,4,5,6,7]))