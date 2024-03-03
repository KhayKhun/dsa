# my solution
def isPalindrome(x):
        s,i,j = str(x),0,len(str(x)) -1

        while i < j:
                print(s[i],s[i])
                if s[i] == s[j]:
                        i += 1
                        j -= 1
                else:
                        return False
        return True     
        
# other faf solution
def isPalindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]
        # if string = 'abc'
        #  string[::-1] = 'cba'

print(isPalindrome(210012))
print(isPalindrome(123))