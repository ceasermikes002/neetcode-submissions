import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # ── Step 1: Build a min-heap of the first k elements ─────────────────
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # transform the slice into a heap in O(k) time
        
        # ── Step 2: Process the remaining elements ───────────────────────────
        for num in nums[k:]:
            if num > min_heap[0]:  # only add to heap if the element is larger
                heapq.heappushpop(min_heap, num)  # maintain heap size of k
        
        # ── Step 3: Return the root of the heap (smallest of the k largest) ──
        return min_heap[0]  # the k-th largest is now at the root