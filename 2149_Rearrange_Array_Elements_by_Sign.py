class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # naive approach, take the integers in their respective orders 
        # then place them, one after the other 
        posInts, negInts, i = [], [], 0
        for num in nums:
            if num >= 0:
                posInts.append(num)
            else:
                negInts.append(num)
        ans = []
        while i < len(posInts):
            ans.append(posInts[i])
            ans.append(negInts[i])
            i+=1
        return ans