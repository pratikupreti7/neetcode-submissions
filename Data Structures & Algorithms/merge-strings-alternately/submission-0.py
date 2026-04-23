class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
# word1 = "ab", word2 = "abbxxc"
# parts=[a,a,b,b,]
        w1=0
        w2=0

        parts=[]

        while w1<len(word1) and w2<len(word2):
            parts.append(word1[w1])
            parts.append(word2[w2])
            w1+=1
            w2+=1

        while w1<len(word1):
            parts.append(word1[w1])
            w1+=1
            
        while w2<len(word2):
            parts.append(word2[w2])
            w2+=1
        
        return ''.join(parts)






        