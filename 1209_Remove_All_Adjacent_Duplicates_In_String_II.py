class Solution:
    def removeDuplicates(self, s, k):
        # Use a stack to store the duplicate chars, the hash tag is for a dummy element to avoid an empty stack
        stack = [['#', 0]]
        # Iterate through the string
        for c in s:
            # If the next character c is the same as the last one, increment the count
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            # Otherwise push a pair (c,1) into the stack
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)
        