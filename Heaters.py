class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters) - 1

        i = 0
        res = 0

        for house in houses:
            while i < n and heaters[i] + heaters[i+1] <= house * 2:
                i += 1
            res = max(res, abs(heaters[i] - house))

        return res
