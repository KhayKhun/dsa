from collections import defaultdict
class Solution:
    def removeAnagrams(self, words):
        d = defaultdict(list)
        count = 0
        for i in words:
            val = ''.join(sorted(i))
            print(type(val),val,type(i),i,val == i)
            if not d[val]:
                d[val] = i
            elif val == i and d[val] == i:
                d[count] = i
                count += 1
                print('case')

        return d.values()                

print(Solution().removeAnagrams(['a','b','a']))