class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        total,d = 0,0
        for i in possible:
            if i: total += 1
            else: total -= 1

        for key,val in enumerate(possible[:-1]):
            if val:
                total -= 1
                d += 1 
            else:
                total +=1
                d -= 1
            
            if d > total: return key + 1
                
        return -1
            