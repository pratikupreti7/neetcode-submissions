class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # approach1 
        # sort each item 
        # if item. key already exist then append 
        # else create it as key and add the item 
        # return list.values()
        maps={} # O(n) space 
        for s in strs:
            key=''.join(sorted(s))

            if key in maps:
                maps[key].append(s)
            else:
                maps[key]=[s]
        

        answer=[]

        for val in maps.values():
            answer.append(val)

        return answer


        
            
            






        