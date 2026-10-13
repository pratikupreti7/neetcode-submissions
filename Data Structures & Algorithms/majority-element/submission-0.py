class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # hashmap 

        maps={}

        for i in nums:

            if i in maps:
                maps[i]+=1
            
            else:
                maps[i]=1

        


        max_val=-1
        max_num=-1

        for key,val in maps.items():

            if val>max_val:
                max_num=key
                max_val=val

        return max_num






        


            

            
        