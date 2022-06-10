class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #need 3 temporary variables to find the longest substring
        max_length, start = 0,0
        seen = {}

        #start walking through the string of characters, one at a time
        for i in range(len(s)):
            
            #1: check if the current character is in the seen map,
            #this implies that we have already seen it and 
            #have it stored in it's corresponding index.

            #2: if it is in there and the start index is <= that index 

            #1                  #2
            if s[i] in seen and start <= seen[s[i]]:

                #update start to the last seen duplicate's index+1.
                start = seen[s[i]] + 1
                #this will put start at just past the current
                #value's last seen duplicate
            
            else:
                #calculate the longest substring seen so far by:
                #taking the current index (i) and subtracting the start index
                #if that value is larger than max_length, set it to ml
                max_length = max(max_length, i - start + 1)

            #update seen map to contain the current value that has been processed
            seen[s[i]] = i
        return max_length