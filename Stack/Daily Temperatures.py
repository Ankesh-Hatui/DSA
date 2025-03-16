'''
* LeetCode : 739
* T.C : O(N)
* S.C : O(N) # space for stack
'''
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        n = len(temp)
        ans = [0]*n
        for i in range(n):
            while stack and temp[i]>temp[stack[-1]]:
                ind = stack[-1]
                ans[ind] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans

