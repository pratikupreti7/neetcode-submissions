import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]


        for x,y in points:
            dist=x*x+y*y

            heapq.heappush(heap,(dist,x,y))

        answer=[]

        while k>0:
            dist,x,y=heapq.heappop(heap)
            answer.append([x,y])
            k=k-1

        return answer

            



        