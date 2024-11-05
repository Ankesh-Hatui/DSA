LC : 2914
TC : O(N)
SC: O(1)
class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s)

        i,j=0,0
        exch=0
        while i<n and j<n:
            while j<n and s[i]==s[j]:
                j+=1
            if j<n and ((j-i)%2)!=0:
                exch+=1
                j=j+1
                i=j
                continue
            i=j
        return exch
