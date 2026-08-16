class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_k=0
        k=0
        for num in nums:
            if num==1:
                k+=1
                max_k=max(max_k,k)

            else:
                k=0
        
        return max_k
        