#Leetcode : 2275
#Time_Complexiety:O(n*32)
#space Complexity:O(1)

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans=0

        for i in range(32):

            cnt=0
            for c in candidates:
                if c & (1<<i):
                    cnt+=1
            
            ans=max(ans,cnt)
        return ans
