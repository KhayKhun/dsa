class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}
        color_count = {}
        res = []

        for b, c in queries:
            if b in ball_colors:
                old_color = ball_colors[b]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]

            ball_colors[b] = c

            if c in color_count:
                color_count[c] += 1
            else:
                color_count[c] = 1

            res.append(len(color_count))

        return res
