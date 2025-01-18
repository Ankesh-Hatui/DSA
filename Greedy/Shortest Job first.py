'''
* GFG ='https://www.geeksforgeeks.org/problems/shortest-job-first/1'
* T.C : O(NlogN)
* S.C : O(N)
'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import math
def cil(n,d):
    return (n+d-1)//d
class Solution:
    def solve(self, bt):
        # Code here
        bt.sort()
        total=0
        wt=[0 for _ in range(len(bt))]
        wait=0
        for i in range(1,len(bt)):
            wt[i]=bt[i-1]+wt[i-1]
        return sum(wt)//len(bt)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        bt = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(bt)
        print(res)
        print("~")
# } Driver Code Ends