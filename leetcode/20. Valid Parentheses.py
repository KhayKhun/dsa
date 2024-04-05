class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        stack = []
        for i in s:
            if i in ['{','[','(']:
                stack.append(i)
            else:
                if len(stack) == 0: return False
                l = stack[-1]
                if (l == '{' and i == '}') or (l == '[' and i == ']') or (l == '(' and i == ')'):
                    stack.pop()
                else: return False
        
        return len(stack) == 0

            

        