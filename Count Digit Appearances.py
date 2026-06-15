class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        num = str(nums)
        ans = num.count(str(digit))

        return ans
