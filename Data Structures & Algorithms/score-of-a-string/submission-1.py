class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for c in range(0, len(s)-1):
            score += abs(ord(s[c]) - ord(s[c+1]))
        return score

        