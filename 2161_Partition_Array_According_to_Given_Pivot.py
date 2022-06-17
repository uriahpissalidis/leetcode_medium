class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        biggerThan = []
        pivots = []
        lessThan = []
        for num in nums:
            if num < pivot:
                lessThan.append(num)
            if num == pivot:
                pivots.append(num)
            if num > pivot:
                biggerThan.append(num)

        for num in pivots:
            lessThan.append(num)
        for num in biggerThan:
            lessThan.append(num)
        return lessThan