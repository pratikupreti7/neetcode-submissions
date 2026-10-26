class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6], target = 7

        maps={}

        for i,num in enumerate(nums):
            find=target-num
            if find in maps:
                return [maps[find],i]

            else:
                maps[num]=i

        return [-1,-1]