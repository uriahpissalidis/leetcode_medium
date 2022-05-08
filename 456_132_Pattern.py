class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] #Keep monotonic strictly decreasing stack
        min_val = nums[0]
        
        for num in nums:
            while stack and stack[-1][0] <= num:
                #Track min value up to this num
                min_val = min(min_val, stack.pop()[0])
                
            #Check if 132 sequence exists. 
            #If stack is not empty, it means that 32 sequence exists. 
            #only need to check min value up to number in stack is less than curr num. 
            if stack and num > stack[-1][1]:
                return True
            #push the current number into the stack 
            stack.append([num, min_val])
        #if this loop terminates, it means the pattern wasn't found in the array
        return False