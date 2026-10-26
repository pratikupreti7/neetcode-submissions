class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        keep=0

        for num in nums:

            if num!=val:

                nums[keep]=num
                keep+=1
        

        return keep



