class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        minHeap, n = [], len(m)

        for i in range(n):
            for j in range(n):
                minHeap.append(m[i][j])

        heapq.heapify(minHeap) # time O( n )

        while k > 1 :
            heapq.heappop(minHeap)
            k -= 1
        return minHeap[0] 