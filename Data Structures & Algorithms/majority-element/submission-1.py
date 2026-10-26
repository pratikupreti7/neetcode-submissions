class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num=nums[0]

        cnt=1
        # # [5,5,1,1,1,5,5]
        #  5 ,1 
        #  5, 2
        #  1, 1
        #  1,0

        for i in nums[1:]:

            if i==num:
                cnt+=1

            else:
                cnt-=1
            
            if cnt<0:
                num=i
                cnt=1
        
        return num

        