class Solution:
    def scoreOfString(self, s: str) -> int:
        diff = []

        for i in range(1,len(s)):
            diff.append(abs(ord(s[i-1]) - ord(s[i])))

        score = sum(diff)

        return score
