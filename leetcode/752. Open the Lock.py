from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends: return -1

        def increase(s, index): 
            return s[:index] + str((int(s[index]) + 1) % 10 ) + s[index + 1:]
        def decrease(s, index): 
            return s[:index] + str((int(s[index]) - 1 + 10) % 10 ) + s[index + 1:]

        visited = set(deadends)
        q = deque([('0000',0)])

        while q:
            current, step = q.popleft()
            if current == target: return step

            for i in range(0,4):
                ic, dc = increase(current,i), decrease(current,i)
                
                if ic not in visited:
                    visited.add(ic)
                    q.append((ic, step + 1))
                    
                if dc not in visited:
                    visited.add(dc)
                    q.append((dc, step + 1))
        
        return -1
    
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"

print(Solution().openLock(deadends,target))
print(Solution().openLock(["0201","0101","0102","1212","2002"],"0202"))

# similar, faster
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        seen = set(deadends)
        if '0000' in seen:
            return -1
        q = deque()
        q.append(('0000', 0))
        seen.add('0000')
        def neis(node):
            for i in range(4):
                for d in (-1, 1):
                    yield node[:i] + str( (int(node[i])+d) % 10) + node[i+1:]
        while q:
            node, dist = q.popleft()
            for nei in neis(node):
                if nei == target:
                    return dist + 1
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, dist + 1))
        return -1