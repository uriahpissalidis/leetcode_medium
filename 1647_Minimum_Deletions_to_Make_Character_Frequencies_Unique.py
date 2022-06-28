class Solution:
    def minDeletions(self, s: str) -> int:
        res=0
        d=Counter(s)
        freq=set()
        for char,count in d.items():
            while count in freq and count>0:
                count-=1
                res+=1
            freq.add(count)
        return res