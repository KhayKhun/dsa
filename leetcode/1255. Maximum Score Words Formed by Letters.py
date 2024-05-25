class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def can_form(w, lc):
            word_cnt = Counter(w)
            for char in word_cnt:
                if word_cnt[char] > lc[char]:
                    return False
            return True
             
        def get_score(word):
            total = 0
            for char in word:
                total += score[ord(char) - ord('a')]
            return total

        letters_cnt = Counter(letters)
        def backtrack(i):
            if i == len(words): return 0
            # skip
            res = backtrack(i+1)
            #include
            if can_form(words[i],letters_cnt):
                for char in words[i]:
                    letters_cnt[char] -= 1
                res = max(res, get_score(words[i]) + backtrack(i + 1))
                for char in words[i]:
                    letters_cnt[char] += 1

            return res

        return backtrack(0)