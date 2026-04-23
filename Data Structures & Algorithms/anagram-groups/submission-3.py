class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # approach1 
        # act
        # [ 0 1 .......t.........00000]
        #
        # 
        res=defaultdict(list)
        for item in strs:
            count=[0]*26

            for i in item:
                count[ord(i)-ord('a')]+=1

            res[tuple(count)].append(item)
        
        return list(res.values())



        


        
            
            






        