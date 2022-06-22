class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use :k to find the 2nd largest element
        heap = nums[:k]
        # swap current node with higher priority child
        heapq.heapify(heap)
        # go through the list one element at a time
        for i in nums[k:]:
            heapq.heappushpop(heap,i)
        return heap[0]