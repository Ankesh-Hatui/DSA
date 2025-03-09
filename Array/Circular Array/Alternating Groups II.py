'''
* Leetcode : 3208
* T.C : O(N + K )
* S.C : O(1)
'''
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        i,j,p=0,0,0
        cnt =0
        while p<(n+k-1):
            # j = p%n
            if p>0 and colors[p%n]==colors[(p%n)-1]:
                i=p
            if (p-i+1)>=k:
                cnt+=1
                i+=1
            
            p+=1
        return cnt
