class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # Sort tokens in ascending order
        i, j, score, max_score = 0, len(tokens) - 1, 0, 0

        while i <= j:
            if power >= tokens[i]:  # Play face-up
                power -= tokens[i]
                score += 1
                max_score = max(max_score, score)
                i += 1
            elif score > 0:  # Play face-down
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break  # No valid moves left

        return max_score

