from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l, r = 0, len(people) - 1

        while l < r:
            first = people[l]
            last = people[r]

            if first + last <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                r -= 1
                count += 1
        
        if l == r: count += 1

        return count

