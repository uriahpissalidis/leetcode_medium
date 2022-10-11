class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # memory efficient bitmask solution
        def bitmasking(output):
            numChars = sum([a.isalpha() for a in s])
            for n in range(2**numChars, 2**(numChars+1)):
                bitmask = bin(n)[3:]
                st, bt = [], 0
                for i in range(len(s)):
                    c = s[i]
                    if c.isalpha():
                        if bitmask[bt] == '0':
                            st.append(c.lower())
                        elif bitmask[bt] == '1':
                            st.append(c.upper())
                        bt += 1
                    else:
                        st.append(c)
                output.append(''.join(st))
        output = []
        bitmasking(output)
        return output
        
        # faster solution
        ans = [""]
        for i in s:
            if i.isdigit():
                ans = [j+i for j in ans]
            else:
                t1 = [j+i.lower() for j in ans]
                t2 = [j+i.upper() for j in ans]
                ans = t1+t2 
        return ans