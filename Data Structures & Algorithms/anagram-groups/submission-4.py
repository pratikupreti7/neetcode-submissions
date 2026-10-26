class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 

        maps={}
        # key: value 


        for word in strs:

            anagram="".join(sorted(word))

            if anagram in maps:
                maps[anagram].append(word)

            else:
                maps[anagram]=[word]

        
        return list(maps.values())









        
        