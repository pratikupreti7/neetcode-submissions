class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # n log n 
        target=0
        answer=[]
        for i,num in enumerate(nums):

            # pointers start and end
            start=i+1
            end=len(nums)-1
            # starting check for dups 
            if i>0 and nums[i]==nums[i-1]:
                continue
            while start <end:
                s=num+nums[start]+nums[end]
                if s >target:
                    end=end-1
                elif s<target:
                    start=start+1

                else:
                    answer.append([num,nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1 

        return answer