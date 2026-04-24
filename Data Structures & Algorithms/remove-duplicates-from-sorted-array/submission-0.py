class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # [1,1,2,3,4]

        write=0
        i=0
        while i<len(nums):
            j=i
            while j<len(nums) and nums[i]==nums[j]:
                j=j+1
            
            nums[write] = nums[i]
            write += 1
            i=j

        return write







    

        



        