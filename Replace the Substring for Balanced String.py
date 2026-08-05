class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        left = 0
        ans = n
        ctr = Counter(s) 
        
        for right in range(n):
            ctr[s[right]] -= 1

            while left < n and 4*max(ctr.values()) <= n:
                ans = min(ans, right-left+1) 
                ctr[s[left]] += 1 
                left += 1

        return ans
