def bagOfTokensScore(tokens, power):
        tokens.sort()
        p = power
        score = 0
        current = tokens
        
        while len(current) and p >= current[0]:
            # face-up as much as possible from smallest
            while len(current) and p >= current[0]:
                p = p-current[0]
                current.remove(current[0])
                score += 1
            # face-down that last(greatest) token
            if len(current) > 1 and score > 0:
                p+= current[-1]
                current.pop()
                score -= 1
        
        return score
tokens = [4903,8812,6101,4671,6323,3378,1243,6825,6220,7885,1271,9117,7993,9168,8725]
power = 6810

print(bagOfTokensScore(tokens, power))

