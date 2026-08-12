class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-1001]
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
