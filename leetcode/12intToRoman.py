# my soltion (beats 6%) ;)
def intToRoman(num: int) -> str:
        symbols = ['I','IV', 'V','IX' ,'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
        values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        res = ""

        while num > 0:

            for i in values:
                if i <= num:
                    largest = i
            
            num -= largest
            print('largest',largest,res)
            
            print('index',values.index(largest))
            res += symbols[values.index(largest)]

        return res
    
# other's solution (beats 45%)
class Solution:
    def intToRoman(self, num: int) -> str:
        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        
        # Result Variable
        r = ''
        
        
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num-=n
        return r
    
print(intToRoman(1994))