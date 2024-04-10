from typing import List
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        res = [0] * len(deck)
        q = deque(range(len(deck))) # store indices

        for c in deck:
            i = q.popleft()
            res[i] = c
            print(q,res)
            if q:
                next_card = q.popleft()
                q.append(next_card)
                print(q)
        
        return res

