class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome_range(i, j):
            # standard two-pointer palindrome check on s[i..j]
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                # match, keep going
                left += 1
                right -= 1
            
            else:
                # MISMATCH — spend the one free deletion
                # Try skipping left  → check s[left+1 .. right]
                # Try skipping right → check s[left    .. right-1]
                # Return True if either is a palindrome, else False
                return is_palindrome_range(left+1,right) or is_palindrome_range(left,right-1)

        return True

        



        