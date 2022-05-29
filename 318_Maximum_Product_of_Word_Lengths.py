class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        signature = {w:set(w) for w in words}
        max_product, N = 0, len(words)
        for i in range(N):
            for j in range(i+1, N):
                # Intersection of two sets
                if bool(signature[words[i]] & signature[words[j]]) == False:
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product