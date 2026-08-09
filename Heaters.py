class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        distances = []

        for house in houses:
            min_dist = float('inf')
            for heater in heaters:
                min_dist = min(min_dist, abs(heater - house))
            distances.append(min_dist)

        return max(distances)
