from time import *
# my solution (beats 66%)
def minimumLength(s):
        s_time = time()
    
        """
        :type s: str
        :rtype: int
        """
        while len(s) > 1 and s[0] == s[-1]:
            match_char = s[0]
            while len(s) and s[0] == match_char:
                s = s[1:]
            while len(s) and s[-1] == match_char:
                s = s[:-1]
        e_time = time()
        return (len(s), e_time-s_time)
                
# other solution  
# def minimumLength(s):
#         left, right = 0, len(s) - 1
        
#         while left < right and s[left] == s[right]:
#             char = s[left]
#             while left <= right and s[left] == char:
#                 left += 1
#             while right >= left and s[right] == char:
#                 right -= 1
        
#         return right - left + 1  
        
s = "ccabbaccbabcbccaaabbaaaaccc"
result = minimumLength(s)
print(result)