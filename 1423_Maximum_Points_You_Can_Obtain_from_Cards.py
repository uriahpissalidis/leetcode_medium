class Solution:
    def maxScore(self, cardPoints: List[int], K: int) -> int:
        curr = best = sum(cardPoints[:K])
        k = K -1
        step = 1 
        while k >= 0:
            curr -= cardPoints[k]
            print('cp,', curr)
            k -=1
            curr += cardPoints[-step]
            print('step', curr)
            step +=1
            best = max(best, curr)
        return best