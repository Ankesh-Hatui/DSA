"""
Leetcode : 3254
T.C : O(N^2)

S.C : O(1)

# Brute Force
"""

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        if k==1:
            ans=nums
            return ans
        for i in range(len(nums)-k+1):
            maxi=nums[i]
            prev=nums[i]
            for j in range(i+1,len(nums)):
                
                if prev>=nums[j] or abs(nums[j]-prev)>1:

                    maxi=-1
                    break
                maxi=max(maxi,nums[j])
                prev=nums[j]
                if (j-i+1==k):
                    break
                
            ans.append(maxi)    

        return ans
