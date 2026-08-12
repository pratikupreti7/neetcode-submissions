class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxOnes=0 #2
        one=0
        for i,num in enumerate(nums):
            if num==1:
                one+=1
            else:
                maxOnes=max(maxOnes,one)
                one=0

        return max(maxOnes, one)






            

        