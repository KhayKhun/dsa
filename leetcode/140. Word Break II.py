class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        if s == '': return ['']
        result = []
        for word in d:
            if word in s and s.index(word) == 0:
                remain = s[len(word):]
                ways = self.wordBreak(remain, d)
                res = [ word+' ' + w if w != '' else word for w in ways ]
                for r in res:
                    result.append(r)
        return result
            