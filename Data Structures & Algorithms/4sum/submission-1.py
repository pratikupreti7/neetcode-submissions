class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # n log n 
        answer=[]
        for j,num2 in enumerate(nums):
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            for i in range(j+1,len(nums)):
                # pointers start and end
                start=i+1
                end=len(nums)-1
                # starting check for dups 
                if i>j+1 and nums[i]==nums[i-1]:
                    continue
                while start <end:
                    s = nums[i] + nums[j] + nums[start] + nums[end]
                    if s >target:
                        end=end-1
                    elif s<target:
                        start=start+1

                    else:
                        answer.append([nums[i], nums[j], nums[start], nums[end]])
                        start+=1
                        end-=1
                        while start<end and nums[start]==nums[start-1]:
                            start+=1
                        while start<end and nums[end]==nums[end+1]:
                            end-=1 

        return answer
        