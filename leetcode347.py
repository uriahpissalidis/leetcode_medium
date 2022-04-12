class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        """
        1. Create a dictionary freqs that maps each count value in c to 
        a bucket index in a sparse bucket array, ranked. 
        
        2. Order the buckets in a way that ensures the highest 
        frequency elements are stored in ranked[0], the second 
        highest frequency elements in ranked[1], etc.

        3. Create ranked sparsely with one list for each actual frequency 
        present in freqs. This means we never need to allocate space 
        for a lot of empty lists that we will never use.
        
        4. Walk through our buckets in ranked (ordered from highest to 
        lowest frequency) and take the first k elements, without 
        bothering to chain together lists of elements below the top 
        k frequencies.
        """
        c = Counter(nums)
        freqs = {v : 0 for v in c.values()} #1
        i = len(freqs) - 1
        for freq in range(len(nums) + 1):
            if freq in freqs:
                freqs[freq], i = i, i - 1 #2
        ranked = [[] for _ in range(len(freqs))] #3
        for elem, freq in c.items(): 
            ranked[freqs[freq]].append(elem)
        i, res = 0, [0] * k
        while k:
            j = min(k, len(ranked[i]))
            for m in range(j):
                res[m + len(res) - k] = ranked[i][m]
            i, k = i + 1, k - j
        return res

#Solution 2
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1)
        if k == len(nums):
            return nums
        
        # O(N)
        # Find frequencies for each number in the input array
        # {num1 -> freq1, num2 -> freq2, ...}
        counts = Counter(nums)
        
        # O(N)
        # Transform the frequencies to be of the form: [(freq1, num1), (freq2, num2), ...] to make it work with Python `heapq._heapify_max`
        # This transformation is not necessary if using `heapq.nlargest` but that creates a new heap which is an O(NlogK) operation 
        # while heapify is an O(N) operation
        counts = [(freq, num) for num, freq in counts.items()]
        
        # O(N)
        # Heapify
        heapq._heapify_max(counts)
        
        # O(KlogK) or O(NlogN) if N = K
        # Return top K elements from the heap
        return [heapq._heappop_max(counts)[1] for _ in range(k)]