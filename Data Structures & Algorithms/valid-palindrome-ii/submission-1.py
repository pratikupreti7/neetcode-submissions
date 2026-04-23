class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindormeCheker(i,j):

            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        
        start=0
        end=len(s)-1


        while start<end:
            if s[start]==s[end]:
                start+=1
                end-=1
            
            else:
                return palindormeCheker(start+1,end) or palindormeCheker(start,end-1)


        return True


        
