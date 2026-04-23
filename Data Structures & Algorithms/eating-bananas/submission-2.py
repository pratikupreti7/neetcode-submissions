class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start,end=1,max(piles)

        res=end
        while start<=end:
            k=start+(end-start)//2

            time=0
            for pile in piles:
                time+=math.ceil(float(pile)/k)

            if time<=h:
                res=min(res,k)
                end=k-1

            else:
                start=k+1

        return res


            

            










        