Leetcode: 3163
// TC O(N)
// SC O(1)

class Solution:
    def compressedString(self, word: str) -> str:
        i,j=0,0
        n=len(word)
        ans=''
        while i<n and j<n:

            while j<n and word[i]==word[j] and j-i<9:
                j+=1
            
            ans+=f'{j-i}'+word[i]
            i=j
        return ans
