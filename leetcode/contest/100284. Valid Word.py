class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        has_vowel = False
        has_consonant = False
        
        for char in word:
            if not char.isalpha() and not char.isdigit():
                return False
            
            if char in vowels:
                has_vowel = True
            elif char.isalpha():
                print(char)
                has_consonant = True
        
        return has_vowel and has_consonant

# Example usage:
solution = Solution()
print(solution.isValid("UuE6"))