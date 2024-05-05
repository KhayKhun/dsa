from collections import defaultdict
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = defaultdict(int)
        i = 0
        j = k
        
        while j <= len(word):
            d[word[i:j]] += 1
            i += k
            j += k
        
        return sum(d.values()) - max(d.values())

# Example usage:
solution = Solution()
print(solution.minimumOperationsToMakeKPeriodic("leetcodeleet", 4))  # Output: 1
print(solution.minimumOperationsToMakeKPeriodic("leetcoleet", 2))    # Output: 3
