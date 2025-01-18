'''
/*
* Leetcode : 503
* T.C : O(N)
* S.C : O(N)
*/
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Create Circular array which overcome traversal problem
        n=len(nums)
        stack=[]
        res=[-1 for _ in range(n)]
        for i in range((2*n)-1,-1,-1):
            el=nums[i%n]
            while stack and stack[-1]<=el:
                stack.pop()
            if stack:
                res[i%n]=stack[-1]
            stack.append(el)
        return res