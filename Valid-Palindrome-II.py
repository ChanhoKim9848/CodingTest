class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                delete_i = s[l+1:r+1]
                delete_j = s[l:r]
                return delete_i==delete_i[::-1] or delete_j==delete_j[::-1]
            l+=1
            r-=1
        return True