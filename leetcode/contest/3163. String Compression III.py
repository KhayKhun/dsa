class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        res = ""
        while i < len(word):
            
            count = 1
            while (i < len(word) - 1 and word[i] == word[i + 1]):
                if count >=9 : break
                count += 1
                i += 1
                
            res += str(count) + word[i]
            i += 1
        
        return res