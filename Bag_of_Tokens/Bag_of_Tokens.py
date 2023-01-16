class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        leftpt, rightpt, score = 0, len(tokens) - 1, 0
        tokens.sort()
        while leftpt <= rightpt:
            if tokens[leftpt] <= power:
                power -= tokens[leftpt]
                score += 1
                leftpt += 1
            else:
                if rightpt == leftpt:
                    pass
                elif leftpt == 0:
                    pass
                else:
                    power += tokens[rightpt]
                    score -= 1
                rightpt -= 1    
        return score
