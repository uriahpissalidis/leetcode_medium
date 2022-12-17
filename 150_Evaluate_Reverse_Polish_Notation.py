class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []                
        for t in tokens:                                         
            if t not in '/+-*':
                stack.append(int(t))
            else:
                num = stack.pop()
                if   t == '+': 
                    stack[-1]+=  num
                elif t == '-': 
                    stack[-1]-=  num
                elif t == '*': 
                    stack[-1]*=  num
                else: 
                    stack[-1]= int(stack[-1]/num)    
        return stack[0]
