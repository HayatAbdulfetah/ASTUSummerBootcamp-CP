class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0
        Sum = sum(nums[:k])
        nextSum = Sum
        maxAverage = nextSum /k
        for i in range(k, len(nums)):
            nextSum += nums[i] - nums[i-k]
            average = nextSum /k
            maxAverage = max(maxAverage, average)

        return maxAverage
