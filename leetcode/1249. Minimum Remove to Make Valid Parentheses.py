class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        d = defaultdict(list)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                d['open'].append(i) # store the index
                stack.append(s[i]) # append '('
            if s[i] == ')':
                if len(stack) == 0: # nothing in stack?
                    d['close'].append(i) # append the index of closing parenteses
                else:
                    l = stack.pop()
                    d['open'].pop()
        
        return ''.join([x for i,x in enumerate(s) if i not in d['open']+d['close']])

        