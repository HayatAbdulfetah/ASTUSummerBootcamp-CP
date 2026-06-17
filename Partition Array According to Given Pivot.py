class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        greater = []
        equal = 0

        for n in nums:
            if n < pivot:
                lesser.append(n)
            elif n == pivot:
                equal += 1
            else:
                greater.append(n)

        return lesser + [pivot]*equal + greater    
