class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        # store key as value and value as index 
        # 3 :1
        for i,num in enumerate(nums):
            diff=target-num
            if diff in s:
                return [s[diff],i]
            
            s[num]=i

        
