import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap and in python we can do negative
        stones=[-val for val in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
# f x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
            if x!=y:
                heapq.heappush(stones,-(y-x))

        return -stones[0] if len(stones)>0 else 0

        

        