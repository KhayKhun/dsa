# my solution (beats 82%)
def isHappy(n):    
    """
    :type n: int
    :rtype: bool
    """
    current = n 
    while current != 1 and (current // 10 > 0 or current == 7):
        # double loop and asign to x, 1st: str() the num and make it list, 2nd: int() each and square up
        x = [int(i)*int(i) for i in [i for i in str(current)]]
        current = sum(x)
    
    return current == 1

n = 7
print(isHappy(n))
