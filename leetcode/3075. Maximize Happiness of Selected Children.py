class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        total = 0

        for i in range(k):
            h = happiness.pop() - i
            total += h if h > 0 else 0
        
        return total

        