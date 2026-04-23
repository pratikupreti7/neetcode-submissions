import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=nums
        heapq.heapify(self.heap)
        # make sure we have k sized list
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        # appending to heap
        heapq.heappush(self.heap,val)

        # return k largest

        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]


        
