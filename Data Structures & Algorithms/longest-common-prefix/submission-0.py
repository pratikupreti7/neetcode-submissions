class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        

        prefix=strs[0]

        answer=''
        for i in range(0,len(prefix)):

            for word in strs[1:]:

                if len(word)==i or word[i]!=prefix[i]:

                    return answer

            answer+=prefix[i]

        return answer








        