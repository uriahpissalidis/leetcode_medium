class Solution:
    def minPartitions(self, n: str) -> int:
        maxNum = 0
        
        # the idea is to find the largest character in the string
        # since that will require the most number of 1's to construct
        for char in n:
            integer = int(char)
            if maxNum <= integer:
                maxNum = integer
        return maxNum
        
        # can also be solved with the max function