class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting it first
        # nums = [-1,0,1,2,-1,-4]

        nums.sort()
        # [-4,-1,-1,0,1,2]
        answer=[]
        for i,n in enumerate(nums):
            # i=0 and n = -4
            # -1
             # 2
            start=i+1
            
            end=len(nums)-1

             # skip duplicate "first" values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while start<end:


                s=nums[i]+nums[start]+nums[end]

                            # skip duplicate "first" values
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                if s <0:
                    start=start+1
                
                elif s>0:
                    end=end-1

                else:
                    answer.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                     # skip duplicates at start and end
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

        return answer
                    


        












        