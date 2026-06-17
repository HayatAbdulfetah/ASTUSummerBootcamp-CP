class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i = 0
        n = len(nums)
        ans = 0

        while i < n:
            if nums[i] % 2 != 0  or nums[i] > threshold:
                i += 1
                continue
            
            start = i

            while i + 1 < n and nums[i + 1] <= threshold  and nums[i] % 2 != nums[i + 1] % 2:
                i += 1
            ans = max(ans, i - start + 1)
            i += 1

        return ans
